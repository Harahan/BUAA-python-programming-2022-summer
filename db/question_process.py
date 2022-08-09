import re


def process(original):
    splitQA = re.search(r'(.*)A.(.*)B.(.*)C.(.*)D.(.*)', original)
    ops = {}
    if splitQA:
        ops['question'] = splitQA[1]
        ops['opA'] = splitQA[2]
        ops['opB'] = splitQA[3]
        ops['opC'] = splitQA[4]
        ops['opD'] = splitQA[5]
    print(ops)
    return ops


def format_checker(original):
    splitQA = re.search(r'(.*)A.(.*)B.(.*)C.(.*)D.(.*)', original)
    if splitQA:
        return True
    return False


def ans_process(answers):
    mapping = {'A': 0b1, 'a': 0b1,
               'B': 0b10, 'b': 0b10,
               'C': 0b100, 'c': 0b100,
               'D': 0b1000, 'd': 0b1000}
    result = 0
    for ans in answers:
        if ans in mapping:
            result = result | mapping[ans]
    return result


def get_ans(answers):
    mapping = {0b1: 'A', 0b10: 'B', 0b100: 'C', 0b1000: 'D'}
    result = []
    for i in mapping.keys():
        if answers & i != 0:
            result.append(mapping[i])
    if len(result) == 0:
        return ''
    elif len(result) == 1:
        return result[0]
    else:
        s = result[0]
        for i in range(1, len(result)):
            s = s + '-' + result[i]
        return s