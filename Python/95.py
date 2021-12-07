import re
try:
    ImputFile=open("danezadanie93.txt","r")
    fileContent=ImputFile.read()
    ImputFile.close()
except IOError:
    print("Bład otwierania pliku")
    exit()

litery=[]
Ile=[]

for i in re.sub("[^\w]", " ",  str(fileContent)).split():
    if not i.isalpha():
        continue
    if i not in litery:
        litery.append(i)
        Ile.append(1)
    else:
        Ile[litery.index(i)]+=1
for i in range(len(litery)):
    print(litery[i]+"  "+ str(Ile[i]))