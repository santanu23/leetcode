class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = Node(value)
    
    def remove(self,value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = None
            return
        else:
            ptr = self.head
            while ptr.next:
                if ptr.next.value == value:
                    if ptr.next.next == None:
                        ptr.next = None
                    else:
                        ptr.next = ptr.next.next
                        return
                else:
                    ptr = ptr.next

    def printList(self):
        ptr = self.head
        while ptr:
            print(ptr)
            ptr = ptr.next

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.remove(3)
l.printList()