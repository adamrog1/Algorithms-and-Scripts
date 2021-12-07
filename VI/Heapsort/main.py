

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


tab = [11,1,3,12,15,76,83,23]
kopiec_sort(tab)
n = len(tab)
print("Posortowana tablica: ")
for i in range(n):
    print("%d" % tab[i]),