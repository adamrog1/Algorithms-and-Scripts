
#funkcja która wybiera pivot dzieli tablice na mniejsze pod problemy ustawia pivot tak ze
# elementy na lewo od pivota jako mniejsze od niego i na prawo jako większe od niego

def podzial(tab, low, high):
    i = (low - 1)  #granica na początku przed pierwszym elementem
    pivot = tab[high]  #pivot przyjmuje element ostatni w tablicy

    for j in range(low, high):

        if tab[j] <= pivot:
            i = i + 1 #granica przesowa sie jeśli element jest mniejszy lub równy pivotowi
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[high] = tab[high], tab[i + 1]
    return (i + 1)


def quickSort(tab, low, high):
    #jesli nasz pivot podzielił talbice tak ze jest to pojedynczy element nie trzeba go sortowac
    if len(tab) == 1:
        return tab
    if low < high:

        pi = podzial(tab, low, high)

        #rekurencja
        quickSort(tab, low, pi - 1)
        quickSort(tab, pi + 1, high)


tab = [12,67,2,56,13,55,84,5,9]
n = len(tab)
quickSort(tab, 0, n - 1)
print("Posortowana tablica: ")
for i in range(n):
    print("%d" % tab[i]),