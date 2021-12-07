import cmath

x=complex(input("Podaj liczbe zespolona"))

wynik=(cmath.sqrt((x.real)**2+(x.imag)**2))

print("Moduł z liczby ",x," to", wynik.real)