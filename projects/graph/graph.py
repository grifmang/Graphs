"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # for first commit
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in this graph.')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                # print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

        return v

    def dft(self, starting_vertex):
            """
            Print each vertex in depth-first order
            beginning from starting_vertex.
            """  
            q = Stack()
            q.push(starting_vertex)
            visited = set()
            while q.size() > 0:
                v = q.pop()
                if v not in visited:
                    print(v)
                    visited.add(v)
                    for next_vert in self.get_neighbors(v):
                        q.push(next_vert)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        s.push(starting_vertex)
        v = s.pop()
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(v)
            visited.add(v)
            for next_vert in self.get_neighbors(v):
                s.push(self.dft_recursive(next_vert, visited))
        
        return v
            

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        # print([starting_vertex])
        q.enqueue([starting_vertex])
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            # print(vertex)
            if vertex == destination_vertex:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for new_vert in self.get_neighbors(vertex): # self.vertices[vertex]:
                    new_path = path[:]
                    new_path.append(new_vert)
                    q.enqueue(new_path)
        return visited

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        s.push([starting_vertex])
        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]
            if vertex == destination_vertex:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for new_vert in self.vertices[vertex]:
                    new_path = path[:]
                    new_path.append(new_vert)
                    s.push(new_path)
        return visited

    # def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """

    #     '''
    #     psuedo-code
        
    #     '''
    #     # Don't need a stack or a starting vertex
    #     # Path will need to be passed on each call, as I don't have access to it
    #     # Will need to return something for path when None
    #     # s = Stack()
    #     s.push([starting_vertex])
    #     path = s.pop()
    #     vertex = path[-1]
    #     if visited == None:
    #         visited = set()
    #     if path == None:
            
    #     if vertex == destination_vertex:
    #         return visited
    #     if starting_vertex not in visited:
    #         visited.add(vertex)
    #         for new_vert in self.get_neighbors(vertex):
    #             new_path = path[:]
    #             new_path.append(new_vert)
    #             # print('visited', visited)
    #             # print('vert', vertex)
    #             # print('dest', destination_vertex)
    #             s.push(self.dfs_recursive(new_vert, destination_vertex, visited))

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)
    print(graph)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
