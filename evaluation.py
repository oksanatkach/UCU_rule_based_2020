import json
from NER.process import get_NERs


def coords2lst(annotations):
    coords = dict()
    for class_name in annotations:
        coords[class_name] = set()
        for span in annotations[class_name]:
            coords[class_name].update(list(range(span[0], span[1])))
    return coords


def process_file(text_path, ann_path):
    text = open(text_path, 'r').read()
    matches = get_NERs(text)
    annotations = json.load(open(ann_path, 'r'))

    true_chars = coords2lst(annotations)
    true_chars_flat = set([ char for label in true_chars for char in true_chars[label] ])
    all_chars = set(range(0, len(text)))
    chars_not_true = all_chars - true_chars_flat
    pred_chars = { label: set() for label in annotations.keys() }

    for match in matches:
        char_start = match[0].idx
        char_end = char_start + len(match.text)

        if match.label_ in pred_chars:
            pred_chars[match.label_].update(list(range(char_start, char_end)))

    pred_chars_flat = set([ char for label in pred_chars for char in pred_chars[label] ])
    chars_not_pred = all_chars - pred_chars_flat

    #@todo: count fp, tp, fn, tn
    # the code above prepared four sets of characters:
    # 1. true_chars - a dictionary this characters that belong to each true class (from the annotated, golden corpus)
    # 2. pred_chars - a dictionary this characters that belong to each predicted class (what our model predicted)
    # 3. chars_not_true - a set of characters that were not annotated by any entity (the O class)
    # 4. chars_not_pred - a set of characters that our model classified as O

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    return tp, fp, tn, fn


def process_all(num):
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for ind in range(num):
        text_path = 'dataset/plain_text/text_' + str(ind+1) + '.txt'
        ann_path = 'dataset/annotations/annotations_' + str(ind+1) + '.json'
        this_tp, this_fp, this_tn, this_fn = process_file(text_path, ann_path)
        tp += this_tp
        fp += this_fp
        tn += this_tn
        fn += this_fn

    #@todo: calculate metrics according to the formulars
    accuracy = 0 # a formula should be here!
    recall = 0
    precision = 0
    f_1 = 0

    print(accuracy)
    print(recall)
    print(precision)
    print(f_1)

if __name__ == '__main__':
    # process_all(23)
    process_all(1)
