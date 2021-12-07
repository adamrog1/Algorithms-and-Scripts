class ListNode:
    def __init__(self,element):
        self.element=element
        self.next=None
        self.previous=None

    def hasvalue(self,value):
        if self.element==value: return True
        else: return False

class Lista_dwukierunkowa():
    def __init__(self):
        self.head = None
        self.tail = None

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

        current_index = 1
        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next

            if current_index == index:
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                return

            current_node = next_node
            current_index+=1


    def add_at_index(self, value, index):
        if index < 0:
            return None
        newelement = ListNode(value)
        nextelement = self.getElementWithIndex(index)
        newelement.next = nextelement
        previouselement = self.getElementWithIndex(index - 1)
        if previouselement is None and index == 0:
            self.head.next = newelement
            if nextelement is None:
                self.tail = newelement
            else:
                nextelement.previous = newelement
            return
        elif previouselement is None:
            print("Indeks dodanego elementu jest zbyt wysoki")
            return
        previouselement.next = newelement
        newelement.previous = previouselement
        if nextelement is None:
            self.tail = newelement
        else:
            nextelement.previous = newelement

    def search(self, value):
        current_node = self.head
        node_index = 1
        results = []
        while current_node is not None:
            if current_node.hasvalue(value):
                results.append(node_index)
            current_node = current_node.next
            node_index+=1

        return results




lista2=Lista_dwukierunkowa()
ele1=ListNode(3)
lista2.add(4)
lista2.add(5)
lista2.add(6)
lista2.add(ele1)
lista2.getlist()
lista2.add_at_index(3,1)
print("+++++++")
lista2.getlist()
print(lista2.lenght())
lista2.delete(3)
lista2.getlist()