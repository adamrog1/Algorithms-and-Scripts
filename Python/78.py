print("Podaj elementy tablicy wpisz end jeśli chcesz zakończyć")
list=[]
while(True):
    item=input("Podaj kolejny element")
    if item=="end":
        break
    else: list.append(item)

for item in list:
    print(item)
