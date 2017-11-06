

class StopWords():

    def getStopWords(self):
        file_words = open('stop_words.txt', 'r')
        stop_words = file_words.read()
        return stop_words

    def removeStopWords (self, inputString):
        stop_words = self.getStopWords()
        word_tokens = inputString.split()
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        print(inputString)
        print (filtered_sentence)
        return filtered_sentence

    def setStopWords(self, arq):
        file_words = open(arq, 'r')
        stop_words = file_words.read()
        return stop_words
