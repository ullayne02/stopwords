import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

class StopWords():

    def getStopWords(self):
        file_words = open('stop_words.txt', 'r')
        stop_words = file_words.read()
        return stop_words

    def removeStopWords (self, inputString):
        stop_words = self.getStopWords()
        word_tokens = word_tokenize(inputString)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        print(inputString)
        print (filtered_sentence)
        return filtered_sentence

    def setStopWords(arq):
        file_words = open(arq, 'r')
        stop_words = file_words.read()
        return stop_words
