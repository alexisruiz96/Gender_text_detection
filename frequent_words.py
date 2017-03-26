from os import listdir
from os.path import isfile, join
from collections import Counter
import re


N = 10  # Default number of most frequent words


def readAllFiles():
    mypath = "dataset/"
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print('Reading ' + str(len(files)) + 'files...')
    text = ''
    for f in files:
        file = open(mypath + f, 'r')
        lines = file.readlines()
        for l in lines:
            text += l.strip("\n")
    return text


def mostFrequentWordsOfText(n, text):
    words = re.findall(r'\w+', text)
    low_words = [word.lower() for word in words]
    word_counts = Counter(low_words)
    return word_counts.most_common(n)


def printMenu():
    print('Welcome PNL - lab 2')
    global N
    N = int(input('Type the number of frequent word you want to calculate: '))
    print('Most ' + str(N) + ' frequent words: ')
    f_words = mostFrequentWordsOfText(N, readAllFiles())
    for i, w in enumerate(f_words):
        print(str(i) + ': ' + w[0] + '(' + str(w[1]) + ' times)')


printMenu()
