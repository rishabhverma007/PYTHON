# ...existing code...
class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLinkedlist:
    def __init__(self, head=None):
        self.head = head

    def insertatend(self, value):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def printll(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next

obj = SinglyLinkedlist()
obj.insertatend(10)
obj.insertatend(20)
obj.insertatend(30)
obj.printll()
# ...existing code...