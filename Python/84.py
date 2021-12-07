
def getnumber():
    value = input("Wprowadz liczbe: ")

    try:
        n = int(value)
        print("To liczba calkowita")
        return n

    except ValueError:
        try:
            n = float(value)
            print("To liczba rzeczywista")
            return n

        except ValueError:
            print("Blad!")

print("Podana liczba to: ",getnumber())