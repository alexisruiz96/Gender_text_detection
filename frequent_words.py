from os import listdir
from os.path import isfile, join
from collections import Counter
import re
import sys


N = 10  # Default number of most frequent words
MOST_FREQ = []


def readAllFiles():
    mypath = "dataset/"
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print('Reading ' + str(len(files)) + 'files...')
    text = ''
    for f in files:
        text += readFile(mypath + f)
    return text


def readFile(name):
    text = ''
    file = open(name, 'r')
    lines = file.readlines()
    for l in lines:
        text += l.strip("\n")
    return text


def mostFrequentWordsOfText(n, text):
    words = re.findall(r'\w+', text)
    low_words = [word.lower() for word in words]
    word_counts = Counter(low_words)
    return word_counts.most_common(n)


def freqOfWordInText(text, word):
    count = 0
    all_words = re.findall(r'\w+', text)
    for w in all_words:
        if w == word:
            count = count + 1
    return round(count / len(all_words) * 100, 2)


def featureVectorOfText(text, words):
    return [(freqOfWordInText(text, w), w) for w in words]


def printVectorAsWeka(feature_vect):
    weka_vect = ""
    for item in feature_vect:
        weka_vect += str(item[0]) + " \"" + item[1] + "\", "
    print("[" + weka_vect[:-2] + "]")


def printMostFreq():
    for i, w in enumerate(MOST_FREQ):
        print(str(i) + ': ' + w[0] + '(' + str(w[1]) + ' times)')


def calculateMostNFreq():
    global MOST_FREQ
    print('Most ' + str(N) + ' frequent words: ')
    MOST_FREQ = mostFrequentWordsOfText(N, readAllFiles())


def getAllFeatureVectors():
    global MOST_FREQ
    mypath = "dataset/"
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print('Reading ' + str(len(files)) + 'files...')
    for f in files:
        print('Feature vector for file ' + f + ': ')
        f_vector = featureVectorOfText(readFile(mypath + f), [w[0] for w in MOST_FREQ])
        printVectorAsWeka(f_vector)


def printMenu():
    print('Welcome PNL - lab 2')
    print('Select what you want to do: ')
    option = input('1. Calculate most N frequent words\n2. Calculate features vector\nor type "exit" to finish program execution\n')
    if option == "1":
        global N
        N = int(input('Type the number of frequent word you want to calculate: '))
        calculateMostNFreq()
        printMostFreq()
    elif option == "2":
        print('Calculating feature vector with ' + str(N) + ' most frequent words')
        global MOST_FREQ
        if len(MOST_FREQ):
            getAllFeatureVectors()
        else:
            calculateMostNFreq()
            getAllFeatureVectors()
    elif option == "exit":
        sys.exit(0)
    else:
        print('You have selected invalid menu option')
    printMenu()


printMenu()
