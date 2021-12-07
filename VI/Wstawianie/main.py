def wstawianie(tab):

    for i in range(1, len(tab)):
#zaczynamy od lewej do prawej
        key = tab[i]
#porownujemy element po lewej
        j = i - 1
#jęśli mniejszy niż elementy po lewej przesuwamy o miejsce w lewo aż do skutku
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key


tab = [34,21,35,12,9,3,1]
wstawianie(tab)
print("Posortowana tablica:")
for i in range(len(tab)):
    print("%d" % tab[i])