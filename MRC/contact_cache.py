import os
import torch
import random
import logging
import numpy as np
from torch.utils.data import ConcatDataset


def set_seed(seed = 42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


dir_path = './temp'
output_path = os.path.join(dir_path, 'cached_train_512')
all_features, all_dataset, all_examples = [], [], []

logger = logging.getLogger(__name__)
# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)

# Set seed
set_seed()

file_list = os.listdir(dir_path)
for file in file_list:
    if not file.startswith('cached'):
        continue
    print(file)
    cached_features_file = os.path.join(dir_path, file)
    logger.info("Loading features from cached file %s", cached_features_file)

    features_and_dataset = torch.load(cached_features_file)
    features, dataset, examples = (
        features_and_dataset["features"],
        features_and_dataset["dataset"],
        features_and_dataset["examples"],
    )

    logger.info("finish Loading %s begin concat!", cached_features_file)
    logger.info("this features len %s, this dataset len %s, this examples len %s", len(features),
                len(dataset), len(examples))
    all_features = all_features + features
    all_dataset = ConcatDataset([all_dataset, dataset])
    all_examples = all_examples + examples
    logger.info("all features len %s, all dataset len %s, all examples len %s", len(all_features),
                len(all_dataset), len(all_examples))

logger.info("begin save cache")
torch.save({"features": all_features, "dataset": all_dataset, "examples": all_examples}, output_path)
logger.info("end save cache")
