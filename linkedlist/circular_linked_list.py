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
    def loop(self):
        s_list = self.head
        f_list = self.head
        while (s_list and f_list and f_list.next):
            s_list = s_list.next
            f_list = f_list.next.next
            if s_list == f_list:
                print(f_list)
                return

l = linked_list()
l.add(20)
l.add(4)
l.add(40)
l.add(20)
l.add(10)

l.print_list()

l.head.next.next.next.next = l.head
l.loop()

