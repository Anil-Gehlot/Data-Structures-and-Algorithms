
class Graph:

    # while creating of object, user will specify total
    # no. of vertex in the Graph
    def __init__(self, v_cont) :
        self.vertex_count = v_cont
        self.adj_matrix = [ [0] * self.vertex_count for i in range (self.vertex_count )  ]


    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and  0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("invalid vertex")
    

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and  0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("invalid vertex")
    

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and  0 <= v < self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("invalid vertex")
            return False


    def display(self):
        for row in self.adj_matrix:
            for num in row:
                print(num, end=" ")
            print()



g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)

print(g.has_edge(1,2))
g.remove_edge(1, 2)

g.display()