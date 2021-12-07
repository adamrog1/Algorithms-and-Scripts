def search(pattern, txt):
    P = len(pattern)
    T = len(txt)

    #pętla która tworzy "okienko" które porusza sie po całym stringu
    for i in range(T - P + 1):
        j = 0

        #pętla która sprawdza wszystkie elementy w zależności od długości patternu

        while (j < P):
            if (txt[i + j] != pat[j]):
                #jeśli któraś literka się nie zgadza pętla się kończy
                break
            j += 1

        if (j == P):
            print("tekst znaleziony przy indeksie ", i)
            #wszystko ok zwracamy index



txt = "ala ma kota"
pat = "ma"
search(pat, txt)