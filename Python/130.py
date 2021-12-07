string = input("Podaj zdanie: ")

count = 0

for letter in string.lower():
    if letter in "aeyioąęuó":
        count += 1

print("Ilość samogłosek to: "+count)