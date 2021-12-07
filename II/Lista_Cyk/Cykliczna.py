class ListNode:
    def __init__(self,element):
        self.element=element
        self.next=None
        self.previous=None

    def hasvalue(self,value):
        if self.element==value: return True
        else: return False

class Cykliczna():
    def __init__(self):
        self.head = None
        self.tail = self.head

    def add(self, element):
        if not isinstance(element, ListNode):
            element = ListNode(element)
        if isinstance(element, ListNode):
            if self.head is None:
                self.head = element
                element.previous = None
                element.next = None
                self.tail = element
            else:
                self.tail.next = element
                element.previous = self.tail
                self.tail =element

    def getElementWithIndex(self, index):
        if index < 0:
            return None
        element = self.head.next
        i = 0
        if element is None:
            return None
        while i < index:
            if element.next is None:
                return None
            element = element.next
            i += 1
        return element


    def getlist(self):
        node = self.head
        while node is not None:
            print(node.element)
            node = node.next

    def lenght(self):
        licznik = 0
        node = self.head
        while node is not None:
            licznik += 1
            node = node.next
        licznik=licznik.__str__()
        return "długość to: "+licznik

    def delete(self, index):

        if index < 0:
            return None
        element = self.getElementWithIndex(index)
        if index != 0 and self.getElementWithIndex(index) is None:
            print("Indeks elementu jest zbyt wysoki")
            return
        elif index == 0 and element.next is None:
            self.head.next = None
            self.tail = self.head
            return
        elif index == 0:
            self.head.next = element.next
            element.next.previous = None
            return
        elif element.next is None:
            element.previous.next = None
            self.tail = element.previous
            return
        nextelement = element.next
        previouselement = element.previous
        previouselement.next = element.next
        nextelement.previous = element.previous


    def add_at_index(self, value, index):
        if index < 0:
            return None
        newelement = ListNode(value)
        nextelement = self.getElementWithIndex(index)
        newelement.next = nextelement
        previouselement = nextelement.previous
        if previouselement is None and nextelement is self.head:
            self.add(value)
            return
        elif nextelement == self.head.next and index == 0:
            self.head.next = newelement
            nextelement.previous = newelement
        elif nextelement == self.head.next:
            self.tail = newelement
            nextelement.previous = self.tail
        else:
            nextelement.previous = newelement
        previouselement.next = newelement
        newelement.previous = previouselement

    def find(self, value):
        i = 0
        element = self.head.next
        while 1 == 1:
            if element.value == value:
                return i
            element = element.next
            if element == self.head.next:
                return None
            i += 1