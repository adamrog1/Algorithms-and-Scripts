import random

try:
    inputFile = open("danezadanie85.txt", "r")
    fileList = inputFile.read().splitlines()
    inputFile.close()

except IOError:
    print("Blad otwierania pliku")
    exit()

a = random.randint(0,17)
b = random.choice(fileList)

try:
    outputFile = open("wynikzadanie85.txt", "w")

except IOError:
    print("Blad otwierania pliku")
    exit()

outputFile.write(str(a)+"\n")
outputFile.write(str(b))
outputFile.close()