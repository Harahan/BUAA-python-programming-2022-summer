import argparse
import glob
import json
import logging
import os
import pickle
import random
import timeit
import numpy as np
import torch
from torch.utils.data import ConcatDataset

from tqdm import tqdm, trange

from helper import SquadResult, MyProcessor, squad_convert_examples_to_features_orig
from transformers import (
    MODEL_FOR_QUESTION_ANSWERING_MAPPING,
    WEIGHTS_NAME,
    AdamW,
    BertConfig,
    BertTokenizer,
    BertForQuestionAnswering,
    AutoConfig,
    AutoModelForQuestionAnswering,
    AutoTokenizer,
    get_linear_schedule_with_warmup
)


logger = logging.getLogger(__name__)

MODEL_CONFIG_CLASSES = list(MODEL_FOR_QUESTION_ANSWERING_MAPPING.keys())
MODEL_TYPES = tuple(conf.model_type for conf in MODEL_CONFIG_CLASSES)
ALL_MODELS = sum((tuple(conf.pretrained_config_archive_map.keys()) for conf in MODEL_CONFIG_CLASSES), (),)


def set_seed(args):
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if args.n_gpu > 0:
        torch.cuda.manual_seed_all(args.seed)


def to_list(tensor):
    return tensor.detach().cpu().tolist()


def load_and_cache_examples(args, tokenizer, set_type='train', output_examples=False):
    if args.local_rank not in [-1, 0] and set_type == 'train':
        # Make sure only the first process in distributed training process the dataset, and the others will use the cache
        torch.distributed.barrier()

    # Load data features from cache or dataset file
    input_dir = args.feature_dir if args.feature_dir else r"./temp"
    cached_features_file = os.path.join(
        input_dir,
        "cached_{}_{}_{}".format(
            set_type,
            args.data_start_point,
            str(args.max_seq_length),
        ),
    )

    # # Init features and dataset from cache if it exists
    # if os.path.exists(cached_features_file) and not args.overwrite_cache:
    #     logger.info("Loading features from cached file %s", cached_features_file)
    #     features_and_dataset = torch.load(cached_features_file)
    #     features, dataset, examples = (
    #         features_and_dataset["features"],
    #         features_and_dataset["dataset"],
    #         features_and_dataset["examples"],
    #     )
    # else:
    logger.info("Creating features from dataset file at %s", input_dir)

    if not args.data_dir and ((is_evaluate and not args.predict_file) or (not is_evaluate and not args.train_file)):
        try:
            import tensorflow_datasets as tfds
        except ImportError:
            raise ImportError("If not data_dir is specified, tensorflow_datasets needs to be installed.")

        if args.version_2_with_negative:
            logger.warn("tensorflow_datasets does not handle version 2 of SQuAD.")

        tfds_examples = tfds.load("squad")
        examples = SquadV1Processor().get_examples_from_dataset(tfds_examples, evaluate=set_type == 'train')
    else:
        processor = MyProcessor()
        if set_type == 'dev':
            examples = processor.get_dev_examples(args.data_dir, filename=args.predict_file)
        elif set_type == 'train':
            examples = processor.get_train_examples(args.data_dir, filename=args.train_file)
        elif set_type == 'test':
            examples = processor.get_test_examples(args.data_dir, filename=args.test_file)

    start_point = args.data_start_point
    end_point = min(start_point + args.data_example_span, len(examples))
    logger.info("start: %s; end %s, len(examples): %s", start_point, end_point,len(examples))
    examples = examples[start_point:end_point]
    for exp in examples:
        if exp.context_text.find("那须盐原") != -1:
            examples.remove(exp)
            print("success del 那须盐原")
        elif exp.context_text.find("范廷颂枢机") != -1:
            examples.remove(exp)
            print("success del 范廷颂枢机")
        elif exp.question_text == ' ':
            examples.remove(exp)
            print("success del empty question")

            
    features, dataset = squad_convert_examples_to_features_orig(
        examples=examples,
        tokenizer=tokenizer,
        max_seq_length=args.max_seq_length,
        doc_stride=args.doc_stride,
        max_query_length=args.max_query_length,
        is_training=set_type == 'train',
        return_dataset="pt",
        threads=args.threads,
    )

    if args.local_rank in [-1, 0]:
        # old_features, old_dataset, old_examples = [], [], []
        # if os.path.exists(cached_features_file):
        #     logger.info("Loading features from c  ached file %s", cached_features_file)
        #     features_and_dataset = torch.load(cached_features_file)
        #     old_features, old_dataset, old_examples = (
        #         features_and_dataset["features"],
        #         features_and_dataset["dataset"],
        #         features_and_dataset["examples"],
        #     )
        # logger.info("old features len %s, old dataset len %s, old examples len %s", len(old_features), len(old_dataset),
        #             len(old_examples))

        logger.info("Saving new features into cached file %s", cached_features_file)
        # logger.info("features type %s, dataset type %s, examples type %s", type(features), type(dataset), type(examples))

        # features = old_features + features
        # dataset = ConcatDataset([old_dataset, dataset])
        # examples = old_examples + examples

        torch.save({"features": features, "dataset": dataset, "examples": examples}, cached_features_file)
        logger.info("new features len %s, new dataset len %s, new examples len %s", len(features), len(dataset),
                    len(examples))

    if args.local_rank == 0 and not is_evaluate:
        # Make sure only the first process in distributed training process the dataset, and the others will use the cache
        torch.distributed.barrier()

    if output_examples:
        return dataset, examples, features
    return dataset


def main():
    print("main")
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument(
        "--model_type",
        default=None,
        type=str,
        required=True,
        help="Model type selected in the list: " + ", ".join(MODEL_TYPES),
    )
    parser.add_argument(
        "--model_name_or_path",
        default=None,
        type=str,
        required=True,
        help="Path to pre-trained model or shortcut name selected in the list: " + ", ".join(ALL_MODELS),
    )
    parser.add_argument(
        "--summary",
        default=None,
        type=str,
        help="Model summary",
    )
    parser.add_argument(
        "--output_dir",
        default=None,
        type=str,
        required=True,
        help="The output directory where the model checkpoints and predictions will be written.",
    )

    # Other parameters
    parser.add_argument(
        "--data_dir",
        default=None,
        type=str,
        help="The input data dir. Should contain the .json files for the task."
        + "If no data dir or train/predict files are specified, will run with tensorflow_datasets.",
    )
    parser.add_argument(
        "--feature_dir",
        default=None,
        type=str,
        help="The input feature dir. Should contain the cached_features_file for the task."
    )
    parser.add_argument(
        "--train_file",
        default=None,
        type=str,
        help="The input training file. If a data dir is specified, will look for the file there"
        + "If no data dir or train/predict files are specified, will run with tensorflow_datasets.",
    )
    parser.add_argument(
        "--predict_file",
        default=None,
        type=str,
        help="The input evaluation file. If a data dir is specified, will look for the file there"
        + "If no data dir or train/predict files are specified, will run with tensorflow_datasets.",
    )
    parser.add_argument(
        "--test_file",
        default=None,
        type=str,
        help="The input test file.",
    )
    parser.add_argument(
        "--test_prob_file",
        default=None,
        type=str,
        help="The output test_prob file.",
    )
    parser.add_argument(
        "--config_name", default="", type=str, help="Pretrained config name or path if not the same as model_name"
    )
    parser.add_argument(
        "--tokenizer_name",
        default="",
        type=str,
        help="Pretrained tokenizer name or path if not the same as model_name",
    )
    parser.add_argument(
        "--cache_dir",
        default="",
        type=str,
        help="Where do you want to store the pre-trained models downloaded from s3",
    )

    parser.add_argument(
        "--version_2_with_negative",
        action="store_true",
        help="If true, the SQuAD examples contain some that do not have an answer.",
    )
    parser.add_argument(
        "--null_score_diff_threshold",
        type=float,
        default=0.0,
        help="If null_score - best_non_null is greater than the threshold predict null.",
    )

    parser.add_argument(
        "--max_seq_length",
        default=512,
        type=int,
        help="The maximum total input sequence length after WordPiece tokenization. Sequences "
        "longer than this will be truncated, and sequences shorter than this will be padded.",
    )
    parser.add_argument(
        "--doc_stride",
        default=128,
        type=int,
        help="When splitting up a long document into chunks, how much stride to take between chunks.",
    )
    parser.add_argument(
        "--max_query_length",
        default=32,
        type=int,
        help="The maximum number of tokens for the question. Questions longer than this will "
        "be truncated to this length.",
    )
    parser.add_argument("--do_train", action="store_true", help="Whether to run training.")
    parser.add_argument("--do_eval", action="store_true", help="Whether to run eval on the dev set.")
    parser.add_argument("--do_test", action="store_true", help="Whether to run test on the test set.")
    parser.add_argument("--do_merge", action="store_true", help="Whether to merge test prob.")
    parser.add_argument(
        "--evaluate_during_training", action="store_true", help="Run evaluation during training at each logging step."
    )
    parser.add_argument(
        "--do_lower_case", action="store_true", help="Set this flag if you are using an uncased model."
    )
    parser.add_argument("--do_fgm", action="store_true", help="Whether to run Adv-FGM training.")
    parser.add_argument("--do_pgd", action="store_true", help="Whether to run Adv-PGD training.")
    parser.add_argument("--gc", action="store_true", help="Whether to run optimizer-gc training.")

    parser.add_argument("--per_gpu_train_batch_size", default=8, type=int, help="Batch size per GPU/CPU for training.")
    parser.add_argument(
        "--per_gpu_eval_batch_size", default=32, type=int, help="Batch size per GPU/CPU for evaluation."
    )
    parser.add_argument("--learning_rate", default=5e-5, type=float, help="The initial learning rate for Adam.")
    parser.add_argument(
        "--gradient_accumulation_steps",
        type=int,
        default=1,
        help="Number of updates steps to accumulate before performing a backward/update pass.",
    )
    parser.add_argument("--weight_decay", default=0.0, type=float, help="Weight decay if we apply some.")
    parser.add_argument("--adam_epsilon", default=1e-8, type=float, help="Epsilon for Adam optimizer.")
    parser.add_argument("--max_grad_norm", default=1.0, type=float, help="Max gradient norm.")
    parser.add_argument(
        "--num_train_epochs", default=3.0, type=float, help="Total number of training epochs to perform."
    )
    parser.add_argument(
        "--max_steps",
        default=-1,
        type=int,
        help="If > 0: set total number of training steps to perform. Override num_train_epochs.",
    )
    parser.add_argument("--warmup_ratio", default=0.1, type=float, help="Linear warmup over warmup_ratio.")
    parser.add_argument(
        "--n_best_size",
        default=10,
        type=int,
        help="The total number of n-best predictions to generate in the nbest_predictions.json output file.",
    )
    parser.add_argument(
        "--max_answer_length",
        default=32,
        type=int,
        help="The maximum length of an answer that can be generated. This is needed because the start "
        "and end predictions are not conditioned on one another.",
    )
    parser.add_argument(
        "--verbose_logging",
        action="store_true",
        help="If true, all of the warnings related to data processing will be printed. "
        "A number of warnings are expected for a normal SQuAD evaluation.",
    )
    parser.add_argument(
        "--lang_id",
        default=0,
        type=int,
        help="language id of input for language-specific xlm models (see tokenization_xlm.PRETRAINED_INIT_CONFIGURATION)",
    )
    parser.add_argument("--best_val_f1", type=float, default=0., help="best_val_f1")
    parser.add_argument("--best_val_step", type=int, default=0, help="best_val_step")
    parser.add_argument("--logging_ratio", type=float, default=0.1, help="Log every X updates ratio.")
    parser.add_argument("--save_ratio", type=float, default=0.1, help="Save checkpoint every X updates ratio.")
    parser.add_argument(
        "--eval_all_checkpoints",
        action="store_true",
        help="Evaluate all checkpoints starting with the same prefix as model_name ending and ending with step number",
    )
    parser.add_argument("--no_cuda", action="store_true", help="Whether not to use CUDA when available")
    parser.add_argument(
        "--overwrite_output_dir", action="store_true", help="Overwrite the content of the output directory"
    )
    parser.add_argument(
        "--overwrite_cache", action="store_true", help="Overwrite the cached training and evaluation sets"
    )
    parser.add_argument("--seed", type=int, default=42, help="random seed for initialization")

    parser.add_argument("--local_rank", type=int, default=-1, help="local_rank for distributed training on gpus")
    parser.add_argument(
        "--fp16",
        action="store_true",
        help="Whether to use 16-bit (mixed) precision (through NVIDIA apex) instead of 32-bit",
    )
    parser.add_argument(
        "--fp16_opt_level",
        type=str,
        default="O1",
        help="For fp16: Apex AMP optimization level selected in ['O0', 'O1', 'O2', and 'O3']."
        "See details at https://nvidia.github.io/apex/amp.html",
    )
    parser.add_argument("--server_ip", type=str, default="", help="Can be used for distant debugging.")
    parser.add_argument("--server_port", type=str, default="", help="Can be used for distant debugging.")

    parser.add_argument("--threads", type=int, default=1, help="multiple threads for converting example to features")

    parser.add_argument("--data_start_point", type=int, default=0, help="dataset start point for converting examples")
    parser.add_argument("--data_end_point", type=int, default=100000, help="dataset end point for converting examples")
    parser.add_argument("--data_example_span", type=int, default=100000, help="dataset cache span")
    args = parser.parse_args()

    print("parser")

    # Setup CUDA, GPU & distributed training
    if args.local_rank == -1 or args.no_cuda:
        device = torch.device("cuda" if torch.cuda.is_available() and not args.no_cuda else "cpu")
        args.n_gpu = 0 if args.no_cuda else torch.cuda.device_count()
    else:  # Initializes the distributed backend which will take care of sychronizing nodes/GPUs
        torch.cuda.set_device(args.local_rank)
        device = torch.device("cuda", args.local_rank)
        torch.distributed.init_process_group(backend="nccl")
        args.n_gpu = 1
    args.device = device

    print("cuda")

    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO if args.local_rank in [-1, 0] else logging.WARN,
    )
    logger.warning(
        "Process rank: %s, device: %s, n_gpu: %s, distributed training: %s, 16-bits training: %s",
        args.local_rank,
        device,
        args.n_gpu,
        bool(args.local_rank != -1),
        args.fp16,
    )

    # Set seed
    set_seed(args)

    print("log")

    # Load pretrained model and tokenizer
    if args.local_rank not in [-1, 0]:
        # Make sure only the first process in distributed training will download model & vocab
        torch.distributed.barrier()

    # args.model_type = args.model_type.lower()
    # config = BertConfig.from_pretrained(
    #     args.config_name if args.config_name else args.model_name_or_path,
    #     cache_dir=args.cache_dir if args.cache_dir else None,
    # )
    tokenizer = BertTokenizer.from_pretrained(
        args.tokenizer_name if args.tokenizer_name else args.model_name_or_path,
        do_lower_case=args.do_lower_case,
        cache_dir=args.cache_dir if args.cache_dir else None,
    )
    # model = AutoModelForQuestionAnswering.from_pretrained(
    #     args.model_name_or_path,
    #     from_tf=bool(".ckpt" in args.model_name_or_path),
    #     config=config,
    #     cache_dir=args.cache_dir if args.cache_dir else None,
    # )

    start = args.data_start_point
    end = args.data_end_point
    span = args.data_example_span
    print(start)
    for start_point in range(start, end, span):
        args.data_start_point = start_point
        # dataset, examples, features = load_and_cache_examples(args, tokenizer, set_type='train', output_examples=True)
        dataset, examples, features = load_and_cache_examples(args, tokenizer, set_type='dev', output_examples=True)

if __name__ == "__main__":
    main()
