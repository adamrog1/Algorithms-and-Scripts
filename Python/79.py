tekst=input("Podaj tekst")
wynik=[]
for i in tekst:
    if i in "aeyioąęuó":
        if i not in wynik:
            wynik.append(i)

for i in wynik:
    print(i)
