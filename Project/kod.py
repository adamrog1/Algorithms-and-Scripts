
import matplotlib.pyplot as plt
class Projekt:


    def kontent(self):
        b=[]
        text_file=open("dane.txt","r")
        a =text_file.read().split(',')
        for i in a:
            b.append(int(i))
        print(b)
        c=[3,4,5,6,7]
        print(c)
        plt.plot(c,b)
        plt.plot(b,c)
        plt.savefig("wynik.png")
        plt.savefig("wynik.png")


def stworzstrone():
    no=Projekt()
    no.kontent()

    f=open("wyjscie.html", "w")

    f.write("<!DOCTYPE html>\n")
    f.write("""<html lang="pl">\n""")
    f.write("<head>\n")
    f.write("""\t<meta charset="UTF-8">\n""")
    f.write("\t<title>Projekt Języki Skryptowe</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("\t<img src='wynik.png'>\n")
    f.write("</body>\n</html>")

    f.close()

stworzstrone()