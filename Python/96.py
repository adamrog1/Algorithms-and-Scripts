try:
    inputFile = open("danezadanie96.txt", "r")
    fileContent = inputFile.read()
    inputFile.close()

    outputFile = open("wynikzadanie96.txt", "w")
except IOError:
    print("Blad otwierania pliku")
    exit()

outputFile.write(str(fileContent).upper())
outputFile.close()