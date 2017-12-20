class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.next = temp

    def printx(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def n_th(self, index):
        current = self.head
        length = self.size()
        for i in range(length):
            if(i == len-index+1):
                current = current.next
                print(current.data)
        

l = Linked_list()
l.add(4)
l.add(1)
l.add(45)
l.add(3)
l.add(6)
l.printx()
print(" ")
l.size()
l.n_th(3)
