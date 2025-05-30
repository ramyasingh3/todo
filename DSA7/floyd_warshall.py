from typing import List, Tuple, Dict
import sys

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.dist = [[float('infinity')] * vertices for _ in range(vertices)]
        self.next = [[None] * vertices for _ in range(vertices)]
        
        # Initialize diagonal elements to 0
        for i in range(vertices):
            self.dist[i][i] = 0
            
    def add_edge(self, u: int, v: int, weight: int):
        """Add a directed edge to the graph"""
        self.dist[u][v] = weight
        self.next[u][v] = v
        
    def floyd_warshall(self) -> Tuple[List[List[float]], List[List[int]]]:
        """
        Find shortest paths between all pairs of vertices using Floyd-Warshall algorithm
        
        Returns:
            Tuple[List[List[float]], List[List[int]]]: (distance matrix, next vertex matrix)
        """
        # Initialize distance and next matrices
        dist = [row[:] for row in self.dist]
        next_vertex = [row[:] for row in self.next]
        
        # Floyd-Warshall algorithm
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][k] != float('infinity') and dist[k][j] != float('infinity'):
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
                            next_vertex[i][j] = next_vertex[i][k]
                            
        return dist, next_vertex
        
    def get_path(self, start: int, end: int, next_vertex: List[List[int]]) -> List[int]:
        """
        Reconstruct the shortest path between two vertices
        
        Args:
            start (int): Starting vertex
            end (int): Ending vertex
            next_vertex (List[List[int]]): Next vertex matrix from Floyd-Warshall
            
        Returns:
            List[int]: Shortest path from start to end
        """
        if next_vertex[start][end] is None:
            return []
            
        path = [start]
        while start != end:
            start = next_vertex[start][end]
            path.append(start)
            
        return path
        
    def print_solution(self, dist: List[List[float]], next_vertex: List[List[int]]):
        """Print the shortest paths between all pairs of vertices"""
        print("\nShortest paths between all pairs of vertices:")
        print("Vertex\tDistance\tPath")
        for i in range(self.V):
            for j in range(self.V):
                if i != j:
                    path = self.get_path(i, j, next_vertex)
                    if path:
                        print(f"{i} -> {j}\t{dist[i][j]}\t\t{path}")
                    else:
                        print(f"{i} -> {j}\tNo path exists")

# Example usage
if __name__ == "__main__":
    # Test case 1: Simple graph
    print("Test Case 1: Simple Graph")
    g1 = Graph(4)
    edges = [
        (0, 1, 3),
        (0, 3, 5),
        (1, 0, 2),
        (1, 2, 4),
        (2, 3, 1),
        (3, 2, 2)
    ]
    
    for u, v, w in edges:
        g1.add_edge(u, v, w)
        
    dist, next_vertex = g1.floyd_warshall()
    g1.print_solution(dist, next_vertex)
    print("-" * 50)
    
    # Test case 2: Graph with negative weights
    print("\nTest Case 2: Graph with Negative Weights")
    g2 = Graph(4)
    edges = [
        (0, 1, 4),
        (0, 3, 5),
        (1, 2, -2),
        (2, 3, 1),
        (3, 1, 3)
    ]
    
    for u, v, w in edges:
        g2.add_edge(u, v, w)
        
    dist, next_vertex = g2.floyd_warshall()
    g2.print_solution(dist, next_vertex)
    print("-" * 50)
    
    # Test case 3: Disconnected graph
    print("\nTest Case 3: Disconnected Graph")
    g3 = Graph(5)
    edges = [
        (0, 1, 2),
        (1, 2, 3),
        (3, 4, 1)
    ]
    
    for u, v, w in edges:
        g3.add_edge(u, v, w)
        
    dist, next_vertex = g3.floyd_warshall()
    g3.print_solution(dist, next_vertex)
    print("-" * 50) 