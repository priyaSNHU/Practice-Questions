class binary_tree:
    def __init__(self, root):
        self.key = root
        self.left_node = None
        self.right_node = None

    def insert_left(self,new_node):
        if self.left_node == None:
            self.left_node = binary_tree(new_node)
        else:
            t = binary_node(new_node)
            t.left_node = self.left_node
            self.left_node = t

    def insert_right(self,new_node):
        if self.right_node == None:
            self.right_node = binary_tree(new_node)
        else:
            t = binary_node(new_node)
            t.right_node = self.right_node
            self.right_node = t

    def get_root_node(self):
        return self.key

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def set_root_node(self, val):
        self.key = val


r = binary_tree('a')
print(r.get_root_node())
print(r.get_left_node())
r.insert_left('b')
print(r.get_left_node())
print(r.get_left_node().get_root_node())
r.insert_right('c')
print(r.get_right_node())
print(r.get_right_node().get_root_node())
r.get_right_node().set_root_node('d')
print(r.get_right_node().get_root_node())
                            
