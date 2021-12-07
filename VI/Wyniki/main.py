import random
import time


def babelkowe(tab):
    n = len(tab)

    for i in range(n - 1):
       #przechodzimy przez całą tablice ostatni element jest po końcu jednej iteracji jest na właściwym miejscu, powtarzamy aż wszystkie elementy będą we właściwym miejscu
        for j in range(0, n - i - 1):

           #porównujemy dwa sąsiednie elementy od lewej do prawej jeśli lewy jest większy od prawego zamieniamy miejscami
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]

def kopiec(tab, n, i):
    largest = i  # korzeń
    l = 2 * i + 1  # indeksacja drzewa l=lewy, p=prawy dzieciak
    r = 2 * i + 2

   #jesli istnieje potomek sprawdz czy jest wiekszy od rodzica
    if l < n and tab[largest] < tab[l]:
        largest = l

    #to samo tylko z prawej strony
    if r < n and tab[largest] < tab[r]:
        largest = r

    #zamiana
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        kopiec(tab, n, largest)



def kopiec_sort(tab):
    n = len(tab)

    #tworzenie kopca
    for i in range(n // 2 - 1, -1, -1):
        kopiec(tab, n, i)

    # wyciagamy najwiekszy element pojedynczo i powtarzamy aż do końca
    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        kopiec(tab, i, 0)




def quickSort(tab):

    def podzial(tab, low, high):
        i = (low - 1)  # granica na początku przed pierwszym elementem
        pivot = tab[high]  # pivot przyjmuje element ostatni w tablicy

        for j in range(low, high):

            if tab[j] <= pivot:
                i = i + 1  # granica przesowa sie jeśli element jest mniejszy lub równy pivotowi
                tab[i], tab[j] = tab[j], tab[i]

        tab[i + 1], tab[high] = tab[high], tab[i + 1]
        return (i + 1)

    def Main(tab,low,high):

        #jesli nasz pivot podzielił talbice tak ze jest to pojedynczy element nie trzeba go sortowac
        if len(tab) == 1:
            return tab
        if low < high:

            pi = podzial(tab, low, high)

            #rekurencja
            Main(tab, low, pi - 1)
            Main(tab, pi + 1, high)
    Main(tab,0,len(tab)-1)
    return tab

def mergeSort(tab):
    if len(tab) > 1:
        #podzial na pół
        mid = len(tab) // 2

        L = tab[:mid]
        R = tab[mid:]
        #rekurencja lewej strony
        mergeSort(L)
        #rekurencja prawej strony
        mergeSort(R)

        i = j = k = 0

        # Porównywanie elementów
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1


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

#analiza


Ile=5
lista1000=[]
lista10000=[]
lista100000=[]
for i in range(1000): lista1000.append(random.randint(1, 1000))
for i in range(10000): lista10000.append(random.randint(1, 1000))
for i in range(100000): lista100000.append(random.randint(1, 1000))
czas=""
for i in range(Ile): czas += ("CZAS " + str(i+1)).rjust(20)
print("NAZWA".center(15) + "ILOŚĆ LICZB".center(15) + czas  + "CZAS NAJKRÓTSZY".rjust(20) + "CZAS NAJDŁUŻSZY".rjust(20) + "CZAS ŚREDNI".rjust(20) + "BŁĄD STATYSTYCZNY".rjust(20) + "\n")

def Posortuj(arr, function):
    gaps = []
    gapsString = ""
    for sortingtime in range(Ile):
        unsortedlist = [arr[i] for i in range(len(arr))]
        start = time.time()
        sortedlist = function(unsortedlist)
        stop = time.time()
        gaps.append(round((stop - start) * 1000, 5)) # w milisekundach
    for i in range(Ile): gapsString += (str(gaps[i]) + " ms").rjust(20)

    avg = sum(gaps)/Ile
    err = 0
    for i in range(Ile): err += (gaps[i] - avg)*(gaps[i] - avg)
    err = (err/Ile)**(0.5)

    errString = (str(round(err, 5)) + " ms").rjust(20)
    avgString = (str(round(avg, 5)) + " ms").rjust(20)
    minString = (str(round(min(gaps), 5)) + " ms").rjust(20)
    maxString = (str(round(max(gaps), 5)) + " ms").rjust(20)
    print(function.__name__.center(15) + str(len(arr)).center(15) + gapsString + minString + maxString + avgString + errString)

Posortuj(lista1000, babelkowe)
Posortuj(lista1000, wstawianie)
Posortuj(lista1000, kopiec_sort)
Posortuj(lista1000, mergeSort)
Posortuj(lista1000, quickSort)

print()

Posortuj(lista10000,babelkowe)
Posortuj(lista10000,wstawianie)
Posortuj(lista10000,kopiec_sort)
Posortuj(lista10000,mergeSort)
Posortuj(lista10000,quickSort)

print()

Posortuj(lista100000,babelkowe)
Posortuj(lista100000,wstawianie)
Posortuj(lista100000,kopiec_sort)
Posortuj(lista100000,mergeSort)
Posortuj(lista100000,quickSort)