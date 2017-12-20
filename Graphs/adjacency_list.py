class vertex:
    def __init__(self,key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight):
        self.connected_to [nbr] = weight

    def __str__(self):
        return str(self.id)+ 'connected_to: ' + str([x.id for x in self.connected_to])


    def get_connections(self):
        return self.connected_to

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

class graph:
    def __init__(self):
        self.vertlist = {}
        self.num_verticies = 0

    def add_vertex(self,key):
        self.num_verticies = self.num_verticies + 1
        new_vertex = vertex(key)
        self.vertlist[key] = new_vertex
        return new_vertex

    def get_vertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None
    def __contains__(self, n):
        return n in self.vertlist

    def add_edge(self, t, f, cost = 0):
        if t not in self.vertlist:
            nv = self.add_vertex(t)
        if f not in self.vertlist:
            nv = self.add_vertex(f)
        self.vertlist[t].add_neighbor(self.vertlist[f], cost)

    def get_vertices(self):
        return self.vertlist.keys()
    
    def __iter__(self):
        return iter(self.vertlist.values())
        



g = graph()
for i in range(6):
    g.add_vertex(i)
print(g.vertlist)
g.add_edge(0,1,5)
g.add_edge(0,5,2)
g.add_edge(1,2,4)
g.add_edge(2,3,9)
g.add_edge(3,4,7)
g.add_edge(3,5,3)
g.add_edge(4,0,1)
g.add_edge(5,4,8)
g.add_edge(5,2,1)
for v in g:
    for w in v.get_connections():
        print("(%s, %s)" %(v.get_id(), w.get_id()))





















    
                   
                   
    
