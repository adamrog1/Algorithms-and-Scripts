class Kolejka():
    def __init__(self,size):
        self.tail=0
        self.head=0
        self.items=[None]*size
        self.size=size

    def isempty(self):
        if self.tail==self.head: True
        else :False

    def isFull(self):
        if self.head==self.tail+1: return True
        else: return False

    def enqueue(self,number):
        if self.tail<len(self.items)-1:
            if self.isFull(): print("Kolejka jest pełna")
            else:
                self.items[self.tail]=number
                self.tail+=1
        else:
            if self.head !=0:
                self.items[self.tail]=number
                self.tail=0
            else: print("Kolejka jest pełna")


    def dequeue(self):
        if self.isempty() : print("kolejka jest pusta")
        else:
            liczba = self.items[self.head]
            if self.head < (len(self.items) - 1):
                self.head += 1
            else:
                self.head = 0
            return liczba

kolejka=Kolejka(5)
kolejka.enqueue(3)
kolejka.enqueue(5)
kolejka.enqueue(9)
kolejka.enqueue(2)
print(kolejka.items)
kolejka.enqueue(8)
print(kolejka.dequeue())
print(kolejka.items)
kolejka.enqueue(10)
print(kolejka.items)
kolejka.enqueue(12)
print(kolejka.dequeue())
print(kolejka.items)
kolejka.enqueue(15)
print(kolejka.items)