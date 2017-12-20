class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def printx(self):
        current = self.head
        while current:
            print (current.data)
            current = current.next

    def remove_duplicates(self):
        current = second =  self.head
        while current is not None:
            while second.next is not None:
                
                if second.next.data == current.data:
                    second.next = second.next.next
                else:
                    second = second.next
            current = second = current.next

l = LinkedList()

l.add(10)
l.add(25)
l.add(12)
l.add(15)
l.add(15)
l.add(10)
l.printx()
print(" ")
l.remove_duplicates()
l.printx()
