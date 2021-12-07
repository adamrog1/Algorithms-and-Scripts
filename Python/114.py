import math

liczby=input("in: ")

a=float(liczby.split(",")[0])
b=float(liczby.split(",")[1])

wynik=a/4*1/(math.tan(math.pi/a))*b**2

print(wynik)