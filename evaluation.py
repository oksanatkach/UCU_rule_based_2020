import json
from NER.process import get_NERs


def coords2lst(annotations):
    coords = dict()
    for class_name in annotations:
        coords[class_name] = set()
        for span in annotations[class_name]:
            coords[class_name].update(list(range(span[0], span[1])))
    return coords


def process_file(text_path, ann_path, eval_dict):
    text = open(text_path, 'r').read()
    doc, matches = get_NERs(text)
    annotations = json.load(open(ann_path, 'r'))

    true_chars = coords2lst(annotations)
    # print(true_chars)
    true_chars_flat = set([ char for label in true_chars for char in true_chars[label] ])
    all_chars = set(range(0, len(text)))
    # chars_not_true = all_chars - true_chars_flat
    pred_chars = { label: set() for label in annotations.keys() }

    for match in matches:
        char_start = match[0].idx
        char_end = char_start + len(match.text)

        if match.label_ in pred_chars:
            pred_chars[match.label_].update(list(range(char_start, char_end)))

    pred_chars_flat = set([ char for label in pred_chars for char in pred_chars[label] ])
    chars_not_pred = all_chars - pred_chars_flat

    for label in pred_chars:
        chars_not_true = all_chars - true_chars[label]
        chars_not_pred = all_chars - pred_chars[label]

        eval_dict[label]['tp'] += len(pred_chars[label].intersection(true_chars[label]))

        eval_dict[label]['fp'] += len(pred_chars[label] - true_chars[label])

        eval_dict[label]['tn'] += len(chars_not_true.intersection(chars_not_pred))

        eval_dict[label]['fn'] += len(chars_not_pred.intersection(true_chars[label]))

        print(eval_dict[label]['tp'] + eval_dict[label]['fp'] + eval_dict[label]['tn'] + eval_dict[label]['fn'])

    return eval_dict


def process_all(num):
    eval_dict = {
        'LOCATION': {'tp':0, 'fp':0, 'tn':0, 'fn':0},
        'ORGANIZATION': {'tp':0, 'fp':0, 'tn':0, 'fn':0},
        'CARDINAL': {'tp':0, 'fp':0, 'tn':0, 'fn':0},
        'DATE': {'tp':0, 'fp':0, 'tn':0, 'fn':0},
        'PERSON': {'tp':0, 'fp':0, 'tn':0, 'fn':0},
        'DURATION': {'tp':0, 'fp':0, 'tn':0, 'fn':0},
        'PERCENT': {'tp':0, 'fp':0, 'tn':0, 'fn':0},
        'MONEY': {'tp':0, 'fp':0, 'tn':0, 'fn':0}
    }
    metrics_dict = {
        'LOCATION': {},
        'ORGANIZATION': {},
        'CARDINAL': {},
        'DATE': {},
        'PERSON': {},
        'DURATION': {},
        'PERCENT': {},
        'MONEY': {},
    }

    for ind in range(num):
        text_path = 'dataset/plain_text/text_' + str(ind+1) + '.txt'
        ann_path = 'dataset/annotations/annotations_' + str(ind+1) + '.json'

        eval_dict = process_file(text_path, ann_path, eval_dict)

    for label in metrics_dict:
        print(label)
        tp = eval_dict[label]['tp']
        fp = eval_dict[label]['fp']
        tn = eval_dict[label]['tn']
        fn = eval_dict[label]['fn']

        accuracy = (tp+tn) / (tp+tn+fp+fn)
        if tp+fn == 0:
            recall = 0
        else:
            recall = tp / (tp+fn)
        if tp+fp == 0:
            precision = 0
        else:
            precision = tp / (tp+fp)
        if precision + recall == 0:
            f_1 = 0
        else:
            f_1 = 2 * ((precision*recall) / (precision + recall))

        print('Accuracy: ' + str(accuracy))
        print('Recall: ' + str(recall))
        print('Precision: ' + str(precision))
        print('F1: ' + str(f_1))

if __name__ == '__main__':
    # process_all(23)
    process_all(1)
