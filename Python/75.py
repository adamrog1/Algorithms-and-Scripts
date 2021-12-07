List1 = ["17", 17, "dddddd", 1]
List2 = ["17", 17, "aaaa", 2]

maxLen = max(len(List1), len(List2))

for i in range(maxLen):

    print("Elementy o indeksie " + str(i) + "  =  ", end="")
    if i < len(List1) and i < len(List2):
        if List1[i] == List2[i]:
            print("Sa takie same")
            continue
    if i < len(List1):
        print("Lista 1: " + str(List1[i]), end="")
    if i < len(List2):
        if i < len(List1):
            print(",  ", end="")

        print("Lista 2: " + str(List2[i]), end="")
    print(" ")

