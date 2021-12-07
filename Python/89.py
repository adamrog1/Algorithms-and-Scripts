string = input("Podaj tekst do sprawdzenia: ")

if string == string[::-1]:
    print("Tak, to jest palindrom")
else:
    print("Nie, to nie jest palindrom")