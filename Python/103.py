import re

url = input("Podaj adres url: ")

pattern = re.compile("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")

if pattern.match(url):
    print("Ten adres jest poprawny")
else:
    print("Ten adres nie jest poprawny.")