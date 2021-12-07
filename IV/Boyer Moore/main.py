

NO_OF_CHARS = 256


def badCharHeuristic(string, size):

    badChar = [-1] * NO_OF_CHARS

    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


def search(txt, pattern):

    P = len(pattern)
    T = len(txt)
    badChar = badCharHeuristic(pattern, P)
    i = 0
#porównujemy pattern z tekstem przy tych samych indeksach od tyłu,
#sprawdzamy pattern[i] z tekst[i] jeśli się nie zgadza i w patternie nie ma takiego znaku przechodzimy dalej w tym wypadku o 3
#jeśli taki znak znajduje się gdzieś w naszym szukanym patternie przesuwamy szukanie do tego znaku
    while (i <= T - P):
        j = P - 1
        while j >= 0 and pattern[j] == txt[i + j]:
            j -= 1
        if j < 0:
            print("Tekst zostal znaleziony przy indeksie = "+format(i))
            i += (P - badChar[ord(txt[i + P])] if i + P < T else 1)
        else:
            i += max(1, j - badChar[ord(txt[i + j])])



txt = "ala ma kota"
pattern = "ota"
search(txt, pattern)

