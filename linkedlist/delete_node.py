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
        self.head = temp

    def printx(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def rem(self, data):
        temp = self.head
        if (temp is not None):
            if (temp.data == data):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
 
        temp = None

l = Linked_list()

l.add('a')
l.add('b')
l.add('c')
l.add('d')
l.printx()
print (" ")
l.rem('c')
l.printx()
