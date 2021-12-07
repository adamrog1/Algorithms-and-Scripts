import math
#a
alfa=float(input("Podaj alfa (radiany):"))
beta=float(input("Podaj beta (radiany):"))
wynik=2*math.sin(1/2*(alfa+beta))*math.cos(1/2*(alfa-beta))
print("wynik = " + str(wynik))

#b

print("\nb)")
x = float(input("Podaj x: "))
n = int(input("Podaj n: "))
wynikB = 1

def product(n, a):
    i = 0
    result = 1
    while i < a:
        result = result * (n-i)
        i += 1
    return result

for i in range(1, n + 1):
    wynikB += (product(n, i)*x**i)/math.factorial(i)

print("wynik = " + str(wynikB))

#c

print("\nc)")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = math.sqrt(b**2 - 4*a*c)

wynikC1 = (-b+delta)*2*a
wynikC2 = (-b-delta)*2*a

print("wynik x1 = " + str(wynikC1))
print("wynik x2 = " + str(wynikC2))

#d

print("\nd)")
x = float(input("Podaj x: "))
wynikd = 1

for i in range(1, 20):
    wynikd += (x**i)/math.factorial(i)

print("wynik = " + str(wynikd))

#e

print("\ne)")
x = float(input("Podaj x: "))
l = float(input("Podaj l: "))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

wynikE = a[0]

for i in range(10):
   wynikE += (a[i]*math.cos(math.pi*i*x/l) + b[i]*math.sin(math.pi*i*x/l))

print(wynikE)
