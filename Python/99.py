import calendar

a = int(input("Podaj rok o ktorego chcesz rozpoczac sprawdzanie: "))
b = int(input("Podaj rok na ktorych chcesz zakonczyc sprawdzanie: "))

for year in range(min(a, b), max(a,b)):
    if calendar.isleap(year):
        print("Rok " + str(year) + " jest przestepny.")