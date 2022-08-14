import json

from metrics import squad_evaluate
from helper import MyProcessor

def load_json(path):
    with open(path, mode='r', encoding='utf-8') as fin:
        return json.load(fin)

# exp_dir = './output/temp/final_350.txt'
# pred_dir = './output/temp/final_350_hf_online_result.json'
exp_dir = './output/temp/hanglv.json.txt'
pred_dir = './output/temp/hanglv_hf_online_result.json'
processor = MyProcessor()

examples = processor.get_dev_examples("", filename=exp_dir)
predictions = load_json(pred_dir)

results = squad_evaluate(examples, predictions)
print(results)