from collections import deque

class Graph:
    def __init__(self, v_count):
        self.vertex_count = v_count
        self.adj_list = { v:[] for v in range(self.vertex_count)   }

    
    def add_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append( v )
            self.adj_list[v].append( u )
        else:
            print("invalid vertex")
    
    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:

            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)

            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)
        else:
            print("invalid vertex")
    

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return v in self.adj_list[u]
        else:
            print("invalid vertex")
            return False
        
    def bfs(self, start_vertex):
        visited = [False] * self.vertex_count
        queue = deque([start_vertex])
        visited[start_vertex] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbour in self.adj_list[vertex]:
                # print("neighbour" , neighbour)
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    queue.append(neighbour)
        print()
    
    def dfs(self, start_vertex):
        visited = [False] * self.vertex_count
        stack = deque([start_vertex])
        visited[start_vertex] = True

        while stack:
            vertex = stack.pop()
            print(vertex)

            for neighbour in self.adj_list[vertex]:
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    stack.append(neighbour)
            


    def display(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex} : {edges}")
    




g = Graph(6)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(3, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)

print(g.has_edge(2,4))
g.display()

g.bfs(0)
g.dfs(0)