class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        

l = linked_list()
l.add(8)
l.add(2)
l.add(4)

l.print_list()
l.reverse()
l.print_list()

        
