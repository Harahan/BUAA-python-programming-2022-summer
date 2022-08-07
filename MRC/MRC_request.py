import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

def load_tokenizer(model_path):
    return AutoTokenizer.from_pretrained(model_path)

def load_model(model_path):
    return AutoModelForQuestionAnswering.from_pretrained(model_path)

def extract_ans(question, context, tokenizer, model):
    inputs = tokenizer.encode_plus(question, context, return_tensors="pt")
    outputs = model(**inputs)
    answer_start_scores = outputs[0]
    answer_end_scores = outputs[1]

    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1

    result = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))
    if result in {"[CLS]", "[SEP]"}:
        answer = "no answer"
    else:
        result = result.replace(" ", "")
        answer = result
    return answer


def MRC_function(question, content):
    #模型地址，放置已经训练好的模型
    #todo 把模型位置设置好
    model_path = "./model"
    #加载分词器
    tokenizer = load_tokenizer(model_path)
    #加载模型
    model = load_model(model_path)
    answer = extract_ans(question,content,tokenizer,model)
    print(answer)
    return answer

if __name__ == '__main__':
    MRC_function('我的名字是什么','我叫乔治叔叔，来自BUAA')





