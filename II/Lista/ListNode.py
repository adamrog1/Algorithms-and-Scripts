class ListNode:
    def __init__(self,element):
        self.element=element
        self.next=None

    def hasvalue(self,value):
        if self.element==value: return True
        else: return False

class Lista_jednokierunkowa():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        if not isinstance(element, ListNode):
            element = ListNode(element)
        element.next=None
        if self.head is None:
            self.head = element
        else:
            self.tail.next = element
        self.tail = element

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

    def delete(self,index):
        current_index=1
        node=self.head
        prev_node=None
        while node is not None:
            if current_index==index:
                if prev_node is not None:
                    prev_node.next=node.next
                else:
                    self.head=node.next
            prev_node=node
            node=node.next
            current_index+=1


    def add_at_index(self, value, index):
        if index < 0:
            return None
        newelement = ListNode(value)
        newelement.next = self.getElementWithIndex(index)
        previouselement = self.getElementWithIndex(index - 1)
        if previouselement is None and index == 0:
            self.head.next = newelement
            return
        elif previouselement is None:
            print("Indeks dodanego elementu jest zbyt wysoki")
            return
        previouselement.next = newelement

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





ele1=ListNode(1)
ele2=ListNode(3)
ele3=ListNode(5)
lista=Lista_jednokierunkowa()
lista.add(ele1)
lista.add(ele2)
lista.add(ele3)
lista.getlist()
print(lista.lenght())
lista.add(ele2)
lista.add(4)
lista.add(9)
lista.getlist()
print("=======")
lista.add_at_index(6,2)
lista.getlist()
print(lista.search(3))






