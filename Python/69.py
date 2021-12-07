import random

interwal=1000

punktyokregu=0
punktykwadratu=0

for i in range(interwal**2):
    randx=random.uniform(-1,1)
    randy=random.uniform(-1,1)
    dyst=randx**2+randy**2
    if dyst<=1:
        punktyokregu+=1
    punktykwadratu+=1
    pi=4*punktyokregu/punktykwadratu

print(pi)