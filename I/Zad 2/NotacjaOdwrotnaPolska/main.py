Dane = open("Dane.txt", mode='r')
Wynik=open("Wynik.txt",mode='w')

operatory=set(['+','-','*','/','(',')','^'])
priorytet={'+':1,'-':1,'*':2,'/':2,'^':3}



def notacjaPostfixowa(wyrazenie):
    stos=[]
    postfix=''
    for a in wyrazenie:
        if a not in operatory: postfix+=a
        elif a=='(':
            stos.append('(')
        elif a==')':
            while stos and stos[-1]!='(':
                postfix+=stos.pop()
            stos.pop()
        else:
            while stos and stos[-1]!='('and priorytet[a]<=priorytet[stos[-1]]:
                postfix+=stos.pop()
            stos.append(a)
    while stos:
        postfix+=stos.pop()
    return postfix

def notacjaInfiksowa(wyrazenie):
    stos = []
    infix=''
    znaki = dzialanie.split(' ')
    for znak in znaki:
        if znak.isalnum():
            stos.append(znak)
        elif znak in '+-*/^':
            x = stos.pop()
            y = stos.pop()
            stos.append('(' + x + znak + y + ')')
    infix=(' '.join(stos))
    return infix




opcja='0'
while opcja!='1' and opcja!='2':
    opcja=input('Zamiana na postać postwfiksowa [1] czy na postac infiksowa [2]? ')
    if opcja=='1':
        Dane = open("Dane.txt", mode='w')
        dzialanie=input('Wpisz dzialanie, ktore ma zostac przeksztalcone na notacje postfixowa\n ')
        Dane.write(dzialanie)
        Wynik=open("Wynik.txt",mode='w')
        Wynik.write(notacjaPostfixowa(dzialanie))
        Wynik.close()

    elif opcja=='2':
        dzialanie=input('Wpisz dzialanie, ktore ma zostac przeksztalcone do postaci infiksowej \n[liczby i znaki rozdziel spacja, np. 2 15 +]\n ')
        Dane=open("Dane.txt",mode='w')
        Dane.write(dzialanie)
        Wynik = open("Wynik.txt", mode='w')
        Wynik.write(notacjaInfiksowa(dzialanie))
        Wynik.close()

Odczyt=open("Wynik.txt",mode='r')
Odczyt.seek(0)
print(Odczyt.read())