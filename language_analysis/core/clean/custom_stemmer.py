import sys
from nltk.stem.lancaster import LancasterStemmer 

class Stemmer():

    def __init__(self):
        self.stemmer = LancasterStemmer()

    def stem(self, word_to_be_stemmed):
        return self.stemmer.stem(word_to_be_stemmed)

stemmer = Stemmer()

if __name__ == '__main__':
    outfile = open("/Users/maheshkl/Projects/techOps/lang_analysis/resources/outfile.txt", 'w')
    p = Stemmer()
    if len(sys.argv) > 1:
        for f in sys.argv[1:]:
            infile = open(f, 'r')
            while 1:
                output = ''
                word = ''
                line = infile.readline()
                if line == '':
                    break
                for c in line:
                    if c.isalpha():
                        word += c.lower()
                    else:
                        if word:
                            output += p.stem(word)
                            word = ''
                        output += c.lower()
                print(output)
                outfile.write(output)
            infile.close()
    outfile.close()
