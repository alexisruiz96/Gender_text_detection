from os import listdir
from os.path import isfile, join
from collections import Counter
import re
import sys
import os


N = 10  # Default number of most frequent words
MOST_FREQ = []
F_VECTORS = []


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
        if w.lower() == word:
            count = count + 1
    return round(count / len(all_words), 4)


def featureVectorOfText(text, words, gender):
    return ([(freqOfWordInText(text, w), w) for w in words], gender)


def vectorAsWeka(feature_vect):
    weka_vect = ""
    for item in feature_vect:
        weka_vect += str(item[0]) + ", "
    return "[" + weka_vect[:-2] + "]"


def printMostFreq():
    for i, w in enumerate(MOST_FREQ):
        print(str(i+1) + ': ' + w[0] + '(' + str(w[1]) + ' times)')


def calculateMostNFreq():
    global MOST_FREQ
    print('Most ' + str(N) + ' frequent words: ')
    MOST_FREQ = mostFrequentWordsOfText(N, readAllFiles())


def getAllFeatureVectors():
    global MOST_FREQ, F_VECTORS
    mypath = "dataset/"
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print('Reading ' + str(len(files)) + 'files...')
    for f in files:
        #print('Feature vector for file ' + f + ': ')
        f_vector = featureVectorOfText(readFile(mypath + f), [w[0] for w in MOST_FREQ], f.split("_")[1])
        F_VECTORS.append(f_vector)
        #print(vectorAsWeka(f_vector[0]))


def saveFeatureVectorsToArrf():
    new_path = 'feature_vectors.arff'
    os.remove(new_path)
    new_file = open(new_path, 'w')
    text = "@RELATION p2_pln " + '\n\n\n'
    for x in range(N):
        text += "@ATTRIBUTE" + "\t" + "number" + str(x + 1) + "\t" + "REAL" + '\n'
    text += "@ATTRIBUTE gender {female,male}\n"
    text += '\n\n'
    text += "@DATA" + '\n'

    for v in F_VECTORS:
        text += vectorAsWeka(v[0])[1:-1] + ',' + v[1] + '\n'
    new_file.write(text)
    new_file.close()


def main():
    print('Welcome PNL - lab 2')
    print('Select what you want to do: ')
    option = input('1. Calculate most N frequent words\n2. Calculate features vector and save it to arrf file\nor type "exit" to finish program execution\n')
    if option == "1":
        global N
        N = int(input('Type the number of frequent word you want to calculate: '))
        calculateMostNFreq()
        os.system('clear')
        printMostFreq()
    elif option == "2":
        os.system('clear')
        print('Calculating feature vector with ' + str(N) + ' most frequent words')
        global MOST_FREQ
        if len(MOST_FREQ) == 0:
            calculateMostNFreq()
        getAllFeatureVectors()
        saveFeatureVectorsToArrf()
        print('Calculated features and arff file created')
    elif option == "exit":
        sys.exit(0)
    else:
        print('You have selected invalid menu option')
    main()


main()
