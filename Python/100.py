metki=0
for plec in ["M","K"]:
    for kolor in ["Niebieski","Czarny","Czerwony","Biały","Zielony"]:
        for size in ["S","M","L","XL"]:
            try:
                output=open("wyjsciezadanie100_metka"+str(metki)+".txt","w")
                output.write(plec+", "+kolor+", "+size)
                metki+=1
            except IOError:
                print("Bład otwierania pliku")
                exit()
            finally:
                output.close()
