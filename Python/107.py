#klucz to przesunięcie
def cezar_zaszyfr(plain_text, key):
    encrypted = ""
    for c in plain_text:
#sprawdzanie czy jest duza litera, mala, czy jest cyfrą
        if c.isupper():
            #ord zwraca wartość literki UNICODE
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            #zapisujemy do nowa literke do zaszyfrowanej wiadmomości
            encrypted += c_new

        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new

        elif c.isdigit():
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            encrypted += c

    return encrypted


def cezar_rozszyfr(text, key):

    decrypted = ""

    for c in text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og

        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og

        elif c.isdigit():
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)

        else:
            decrypted += c
    return decrypted

tekst="Ala ma kota"
zaszyfrowany=cezar_zaszyfr(tekst,3)
odszyfrowany=cezar_rozszyfr(zaszyfrowany,3)
print(tekst)
print(zaszyfrowany)
print(odszyfrowany)