def babelkowe(tab):
    n = len(tab)

    for i in range(n - 1):
       #przechodzimy przez całą tablice ostatni element jest po końcu jednej iteracji jest na właściwym miejscu, powtarzamy aż wszystkie elementy będą we właściwym miejscu
        for j in range(0, n - i - 1):

           #porównujemy dwa sąsiednie elementy od lewej do prawej jeśli lewy jest większy od prawego zamieniamy miejscami
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
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
    return tab


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

liczby=[]
try:
    file=open("danezadanie104.txt","r")
    for line in file.read():
        try:
            liczby.append(int(line))
        except ValueError:
            continue
    file.close()
    print(liczby)
    babelkoweplik=open("zadanie104_babelkowe.txt","w")

    for num in babelkowe(liczby):
        babelkoweplik.write(str(num)+"\n")
    babelkoweplik.close()

    wstawianieplik=open("zadanie104_wstawianie.txt","w")
    for num in wstawianie(liczby):
        wstawianieplik.write(str(num)+"\n")
    wstawianieplik.close()

    quickplik=open("Zadanie104_quick.txt","w")
    for num in quickSort(liczby):
        quickplik.write(str(num)+"\n")
    quickplik.close()
except IOError:
    print("Bład otwierania plików")

