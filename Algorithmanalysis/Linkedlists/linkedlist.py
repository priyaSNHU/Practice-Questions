from node import Node

class Linkedlist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    def remove(self, item):
        current = self.head
        found = False
        previous = None
        while current!= None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        if current.get_next() == None:
            previous.set_next = None
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        current = self.head
        previous = None
        while current.get_next() != None:
            current = current.get_next()
        temp = Node(item)
        temp.set_next(current.get_next())
        current.set_next(temp)
        
    def index(self, item):
        current = self.head
        index = 0
        found = False
        while current!= None and not found:
            if current.get_data() == item:
                found = True
            else:
                index += 1
                current = current.get_next()
        return index
    def insert(self, pos, item):
        current = self.head
        index = 0
        while current!= None:
            current = current.get_next()
            index += 1
        if (index == pos):
            temp = Node(item)
            temp.set_next(cuurent.get_next())
            current.get_next(temp)
    def pop(self):
        current = self.head
        if (current.get_next() != None):
            current = current.get_next()
        else:
            temp = current.get_data()
        return temp
    def pop(self, pos):
        current = self.head
        index = 0
        while current!= None:
            current = current.get_next()
            index += 1
        if(index == pos):
            temp = current.get_data()

        return temp


mylist = Linkedlist()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))

print(mylist.index(77))
mylist.insert(3,45)
print(mylist.size())




                
            
                    
            
                
