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

    def printx(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def two_sum(self, first, second):
        prev = None
        temp = None
        carry = 0

        while first is not None or second is not None:

            f_data = 0 if first is None else first.data
            s_data = 0 if second is None else second.data

            add = carry + f_data + s_data

            carry = 1 if add >= 10 else 0

            add = add if add < 10 else add % 10

            # now adding the sum to new linkedlist

            temp = Node(add)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp


            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

            if carry > 0:
                temp.next = Node(carry)

first = linked_list()
second = linked_list()
first.add(8)
first.add(5)
first.add(9)
first.add(1)
print("The first linkedlist: ")
first.printx()

second.add(9)
second.add(1)
second.add(0)
print("The second linkedlist: ")
second.printx()

third = linked_list()
third.two_sum(first.head, second.head)
print("The result linkedlist: ")
third.printx()


    
