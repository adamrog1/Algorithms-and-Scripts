class ListNode:
    def __init__(self,element):
        self.element=element
        self.next=None
        self.previous=None

    def hasvalue(self,value):
        if self.element==value: return True
        else: return False

class Zflaga():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.sentry=None
        self.sentry.previous = self.head
        self.sentry.next = self.head
        self.head.next = self.sentry
        self.tail = self.sentry

    def add(self, element):
        if not isinstance(element, ListNode):
            element = ListNode(element)
        if isinstance(element, ListNode):
            if self.tail == self.sentry:
                element.previous = self.sentry
                element.next = self.sentry
            else:
                element.previous = self.tail
                element.next = self.head.next
                self.head.next.previous = element
            self.tail.next = element
            self.tail = element

    def getElementWithIndex(self, index):
        if index < 0:
            return None
        element = self.sentry.next
        i = 0
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
            return
        element = self.getElementWithIndex(index)
        if element.next is element:
            self.head.next = self.head
            self.tail = self.head
            return
        element.previous.next = element.next
        element.next.previous = element.previous
        if element == self.head.next:
            self.head.next = element.next
        if element.next == self.head.next:
            self.tail = element.previous



    def add_at_index(self, value, index):
        if index < 0:
            return None
        newelement = ListNode(value)
        nextelement = self.getElementWithIndex(index)
        newelement.next = nextelement
        if nextelement is self.sentry:
            self.add(value)
            return
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
        element = self.sentry.next
        self.sentry.value = value
        while 1 == 1:
            if element.value == value:
                if element == self.sentry:
                    return None
                else:
                    return i
            element = element.next
            i += 1

