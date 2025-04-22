
# Implement a Adjacency Matrixes in Graph

class Graph:

    # create a Instances of Adjacency list
    def __init__(self):
        self.adjacencyList = {}

    # Add the Vertex to the adjacency List
    def add_vertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

    # add Edge
    def add_edge(self,u,v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adjacencyList[u]:
            self.adjacencyList[u].append(v)
        if u not in self.adjacencyList[v]:
            self.adjacencyList[v].append(u)

    # Remove Edge
    def remove_edge(self,u,v):
        # u is in adjacency list and find there is any edge between u and v
        if u in self.adjacencyList and v in self.adjacencyList[u]:
            self.adjacencyList[u].remove(v)

        # v is in adjacency list and find there is any edge between u and v
        if v in self.adjacencyList and u in self.adjacencyList[v]:
            self.adjacencyList[v].remove(u)

    
    # Remove Vertex
    def remove_vertex(self,vertex):
        # Check vertex is present in adjacency list or not
        if vertex in self.adjacencyList:
            # Now Remove all the edges connecting to that vertex
            for neighbours in self.adjacencyList[vertex]:
                self.adjacencyList[neighbours].remove(vertex)
            
            del self.adjacencyList[vertex]
    
    
    # Breadth First Search Traversal
    def bfs(self,start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                result.append(vertex)
                visited.add(vertex)
                queue.extend([n for n in self.adjacencyList[vertex] if n not in visited])
        return result
    

    # Depth First Search Traversal
    def dfs(self,start):
        visited = set()
        result = []

        def dfs_recursive(vertex):
            result.append(vertex)
            visited.add(vertex)
            for n in self.adjacencyList[vertex]:
                if n not in visited:
                    dfs_recursive(n)

        # Call the Recursive Function
        dfs_recursive(start)
        return result


    # Display all the Items 
    def display(self):

        for vertex in self.adjacencyList:
            print(vertex, "---->" ,self.adjacencyList[vertex])





