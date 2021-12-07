class KolejkaPrio():
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
            najwyzsza_wart=self.items[self.head]
            najwyzsza_wart_index=self.items[self.head]
            if self.tail>self.head:
                for i in range(self.head,self.tail):
                    if(self.items[i]>najwyzsza_wart):
                        najwyzsza_wart=self.items[i]
                        najwyzsza_wart_index=i
            else:
                for i in range(0,len(self.items)):
                    if(self.tail<=i<self.head):
                        continue
                    if(self.items[i]>najwyzsza_wart):
                        najwyzsza_wart=self.items[i]
                        najwyzsza_wart_index=i

            oldhead = self.items[self.head]
            self.items[self.head] = najwyzsza_wart
            self.items[najwyzsza_wart_index] = oldhead
            value = self.items[self.head]
            if self.head < (len(self.items) - 1):
                self.head += 1
            else:
                self.head = 0
            return value
