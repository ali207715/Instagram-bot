def compute_confusion_matrix(truth_dict, pred_dict, pos_tag, neg_tag):
    from collections import namedtuple
    ConfMat = namedtuple('ConfMat', 'tp tn fp fn')
    a = 0
    b = 0
    c = 0
    d = 0
    for key in pred_dict:
        if pred_dict[key] == neg_tag and truth_dict[key] == neg_tag:
            b += 1
        elif pred_dict[key] == pos_tag and truth_dict[key] == pos_tag:
            a += 1
        elif pred_dict[key] == pos_tag and truth_dict[key] == neg_tag:
            c += 1
        elif pred_dict[key] == neg_tag and truth_dict[key] == pos_tag:
            d += 1

    return ConfMat(a, b, c, d)






if __name__ == "__main__":
    truth_dict = {'em1': 'SPAM', 'em2': 'SPAM', 'em3': 'OK', 'em4':'OK'}
    pred_dict = {'em1': 'SPAM', 'em2': 'SPAM', 'em3': 'OK', 'em4':'OK'}
    cm2 = compute_confusion_matrix(truth_dict, pred_dict, pos_tag='SPAM', neg_tag='OK')
    print(cm2)




def quality_score(tp, tn, fp, fn):
    q = (tp + tn) / (tp + tn + 10 * fp + fn)
    return q




if __name__ == '__main__':
    print(quality_score(1,2,3,4))




def compute_quality_for_corpus(corpus_dir):
    import os
    import utils
    truth_dict = utils.read_classification_from_file(os.path.join(corpus_dir, '!truth.txt'))
    pred_dict = utils.read_classification_from_file(os.path.join(corpus_dir, '!prediction.txt'))
    cm = compute_confusion_matrix(truth_dict, pred_dict, pos_tag = "SPAM", neg_tag = 'OK')
    q = quality_score(cm.tp, cm.tn, cm.fp, cm.fn)
    return q













