n=int(input("Podawaj ile liczb chcesz wpisać"))
liczby=[]
try:
    file = open("zad081.txt", "r")

    for line in file:
        liczby.append(int(line))

    file.close()

except IOError:
    print("Blad otwierania pliku")
suma=sum(liczby)
srednia=suma/n
liczby.sort()
if n%2==1:
    mediana = liczby[n//2]
else:
    l1=(n/2)-1
    l2=(n/2)
    mediana=(l1+l2)/2
print("Suma: ",suma)
print("Srednia: ",srednia)
print("Mediana: ",mediana)