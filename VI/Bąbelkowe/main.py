def babelkowe(tab):
    n = len(tab)

    for i in range(n - 1):
       #przechodzimy przez całą tablice ostatni element jest po końcu jednej iteracji jest na właściwym miejscu, powtarzamy aż wszystkie elementy będą we właściwym miejscu
        for j in range(0, n - i - 1):

           #porównujemy dwa sąsiednie elementy od lewej do prawej jeśli lewy jest większy od prawego zamieniamy miejscami
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]


tab = [123,12,334,12,3,12,54,65,14]

babelkowe(tab)

print("Posortowana tablica: ")
for i in range(len(tab)):
    print("%d" % tab[i]),