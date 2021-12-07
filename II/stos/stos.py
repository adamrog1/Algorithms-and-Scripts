class Stack():
    def __init__(self,size):
        self.top=-1
        self.items=[None]*size
        self.size=size

    def isempty(self):
        if (self.top==0): return True
        else : return False

    def isFull(self):
        if self.top>=len(self.items)-1 : return True
        else: return False

    def push(self,number):
        if self.isFull() : print("Stos jest pełny")
        else :
            self.top += 1
            self.items[self.top]=number


    def pop(self):
        if self.isempty(): print("Stos jest pusty")
        value = self.items[self.top]
        self.top -= 1
        return value

stack=Stack(4)
stack.push(1)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(3)
print(stack.items)
print(stack.pop())
stack.push(3)
print(stack.items)

