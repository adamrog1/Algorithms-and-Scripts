import random

r = int(input("Podaj liczbe wierszy: "))
c = int(input("Podaj liczbe kolumn: "))

for i in range(r):
    for j in range(c):
        print("{:<6}".format(str(random.randint(0,100))), end="")
    print("")