def read_classification_from_file(text):
    with open(text, "r", encoding='utf-8') as f:
        result ={}
        for words in f:
            k, v = words.split()
            result[k] = v
    return result





def write_classification_to_file(cls_dict, fpath):
    with open(fpath, "w", encoding='utf-8') as f_w:
        for key, value in cls_dict.items():
            f_w.write(str(key) + " " + str(value) + '\n')







if __name__ == "__main__":
    fpath = '1/!prediction.txt'
    read_classification_from_file('text.txt')
