#coding:utf-8

'''
AUTHOR : Tanmoy Ghosh (NIT Durgapur)
MODULE REQUIRED : nltk
HOW TO RUN: python language_detector.py <docname>.txt
METHOD : The language detector works on the basis of the stopwords present in the 
         document. Each word is checked whether it is a stopword of any language.
         In this way probability of the document being written in a specific
         language is calculated.
'''

import sys
from nltk import word_tokenize
from nltk.corpus import stopwords

class language_detector:

    def __init__(self):
        self.lang_words = {}
        self.prob = {}

    def get_stopwords(self):
        for lang in stopwords.fileids():
            self.lang_words[lang] = set(stopwords.words(lang))
            self.prob[lang] = 0

    def calc_prob(self,words):

        self.get_stopwords()
        for w in words:
            for lang in self.lang_words:
                if w in self.lang_words[lang]:
                    self.prob[lang]+=1

        total_words = len(words)
        for item in self.prob:
            self.prob[item] = (float(self.prob[item])/total_words)*100


    def solve(self,text):
        words = word_tokenize(text)
        self.calc_prob(words)
        doc_lang = max(self.prob, key=self.prob.get)
        print("The Document is written in " + doc_lang + " language.")


if __name__=='__main__':

    file_name = sys.argv[1]
    file = open(file_name,'r')
    text = file.read()
    lang_det = language_detector()
    lang_det.solve(text)