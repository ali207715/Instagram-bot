import quality
import utils
import os
import email
import re
import string
from collections import Counter
import math


class MyFilter:
# Creating a class for the filter, with two different counters, for words that might be spam or ok.
    def __init__(self):
        self.spam_counter = Counter()  # Loading up a counter for all spam keywords
        self.ok_counter = Counter()  # Loading up counter for all ok words
        self.n_spamemails = 0  # Initializing total numbers of spam words
        self.n_okemails = 0  # Initializing total numbers of ok words
        pass

    def train(self, fpath): # Grabbing all spam and ok keywords for evaluation of the data
        class_dict = utils.read_classification_from_file(os.path.join(fpath, "!truth.txt"))
        for file in class_dict: # Going through each email
            email_list = self.clean_email(fpath, file) # Cleaning up email
            if class_dict[file] =="SPAM": # If tagged SPAM then add to spam words counter
                self.n_spamemails += 1
                self.spam_counter.update(email_list)
            else:
                self.n_okemails += 1 # If tagged OK then add to ok words counter
                self.ok_counter.update(email_list)

    def test(self, fpath):
        pred_dict = {} # Creating empty dict for the predictions
        file_list = os.listdir(fpath)
        for file in file_list:
            if not file.startswith('!'): # Excluding !truth and !pred files
                email_list = self.clean_email(fpath, file) # Cleaning up email
                prob_spam = 0 # Initializing probability of spam words
                prob_ok = 0  # Initializing probability of ok words
                for word in email_list:
                    prob_word_spam = self.spam_counter.get(word, 0) # Grabbing spam words from files
                    prob_word_ok = self.ok_counter.get(word, 0) # Grabbing ok words from files
                    c = (prob_word_spam+1)/self.n_spamemails # Calculating probability of each word over total spam words
                    d = (prob_word_ok+1)/self.n_okemails # Calculating probability of each ok word over total ok words
                    prob_spam += math.log10(c) # Addding up all the probabilities
                    prob_ok += math.log10(d)
                if prob_spam > prob_ok:  # If the probability of SPAM words greater than OK, then email is tagged as SPAM
                    pred_dict[file] = "SPAM"
                else:
                    pred_dict[file] = "OK" # If the probability of OK words is greater than SPAM, email is tagged as OK
        utils.write_classification_to_file(pred_dict, os.path.join(fpath, "!prediction.txt"))  # Writing the results

    def clean_email(self, fpath, file): # Cleaning up the emails provided.
        f = open(os.path.join(fpath, file), "r", encoding='utf-8')
        msg = email.message_from_file(f)
        msg = str(msg) # Converting to string.
        msg = msg.lower() # Lower case everything.
        msg = self.cleanhtml(msg) # Removing html files
        msg = re.sub(r"\d+", " ", msg) # Removing numerical values
        msg = msg.translate(str.maketrans("", "", string.punctuation)) # Removing punctuations
        msg = msg.strip() # Removing leading and following spaces
        msg = msg.split() # Splitting into words
        common_words = ["with", "a", "is", "by", "for", "from", "the", "between", "about", "of", "t", "and", "no", "your","can", "could", "should", "your","b", "c", "d", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
        msg = list(set(msg)) # Appending the words into a list
        for word in common_words: # Removing common words
            if word in msg:
                msg.remove(word)
        p = open("pronouns.txt", "r")  # Removing recurring pronouns
        for word in p:
            if word in msg:
                msg.remove(word)
            return msg

    def cleanhtml(self, msg):  # Cleaning html files
        cleantext = re.sub("<.*?>", " ", msg)
        return cleantext





