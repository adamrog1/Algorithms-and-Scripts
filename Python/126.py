import math

class Kolo:
    def __init__(self,r):
        self.r=float(r)
    def pole(self):
        return math.pi*pow(self.r,2)
    def obwod(self):
        return 2*math.pi*self.r
kolo=Kolo(3)
print(kolo.obwod())
print(kolo.pole())