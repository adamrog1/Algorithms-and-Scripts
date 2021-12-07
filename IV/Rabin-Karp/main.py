d = 256

def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    h = 1
    j = 0

    for i in range(m-1):
        h = (h*d) % q

    p = 0
    t = 0
#algorytm działa tak samo jak naiwny ale tutaj brana pod uwage jest wartość hashowa jeśli wartość hashowa fragmentu jest taka sama jak fragmentu tekstu wtedy zwraca index
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q  #wartosc patternu
        t = (d*t + ord(text[i])) % q  #wartosc porownywanego kawalka

    for i in range(n-m+1):

        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("Pattern znaleziony na indeksie:  " + str(i+1))
        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q


text = "ala ma kota"
pattern = "ota"
q = 1000
search(pattern, text, q)