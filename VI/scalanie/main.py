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


tab = [13,34,51,12,3,2,1,6]
mergeSort(tab)
print("Posortowana tablica:")
for i in range(len(tab)):
    print("%d" % tab[i])