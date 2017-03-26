from os import listdir
from os.path import isfile, join

N = 10 # Default number of most frequent words
def printMenu():
    print('Welcome PNL - lab 2')
    global N
    N = int(input('Type the number of frequent word you want to calculate: '))

printMenu()
print(N)

def readAllFiles():
    mypath = "dataset/"
    aux = 0
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(len(files))
    for f in files:
        if aux < 3:
            print(f)
            aux = aux + 1
        else:
            break

readAllFiles()