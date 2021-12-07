import datetime
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


Ile=1
lista1000=[]
for i in range(1000): lista1000.append(random.randint(1, 1000))
czas=""


def Posortuj(arr, function,file):
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
    file.write(str((function.__name__.center(15)) + str(len(arr)).center(15)) + str(avgString)+ str(errString))
    file.write("\n")

try:
    file=open("raport_"+str(datetime.date.today())+".txt","w")
    file.write("RAPORT ALGORYTMOW SORTOWANIA\n\n")
    file.write("   NAZWA".ljust(13) + "LICZBA SORTOWANYCH PLIKOW".ljust(26) + "SREDNI CZAS".ljust(15) +"ODCHYLENIE STANDARDOWE"+ "\n")
    Posortuj(lista1000,babelkowe,file)
    Posortuj(lista1000,wstawianie,file)
    Posortuj(lista1000,quickSort,file)
    file.close()

    file.close()
except IOError:
    print("Bład otwierania pliku")
