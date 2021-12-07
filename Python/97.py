try:
    outputFile = open("wynikzadanie97.txt", "w")

except IOError:
    print("Blad otwierania pliku")
    exit()

outputFile.write("licznik   suma\n")

i = 0

for i in range(11):
    outputFile.write((str(i).center(5, "*") + "|" + str(i*-4).center(5, "*")) + "\n")

    if i == 0:
        outputFile.write("-"*11 + '\n')


outputFile.close()