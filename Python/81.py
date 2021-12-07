n=int(input("Podawaj ile liczb chcesz wpisać"))
liczby=[]
for i in range(n):
    liczba=int(input("Podaj liczbe"))
    liczby.append(liczba)
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