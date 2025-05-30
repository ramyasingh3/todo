from typing import List, Dict, Tuple
import sys

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        # Initialize distance matrix with infinity
        self.dist = [[float('inf') for _ in range(vertices)] for _ in range(vertices)]
        # Initialize predecessor matrix with None
        self.next = [[None for _ in range(vertices)] for _ in range(vertices)]
        
        # Set diagonal elements to 0
        for i in range(vertices):
            self.dist[i][i] = 0
            
    def add_edge(self, u: int, v: int, weight: float):
        """Add a weighted directed edge to the graph"""
        self.dist[u][v] = weight
        self.next[u][v] = v
        
    def floyd_warshall(self) -> Tuple[List[List[float]], List[List[int]]]:
        """
        Find shortest paths between all pairs of vertices using Floyd-Warshall algorithm
        
        Returns:
            Tuple containing:
            - Distance matrix with shortest path distances
            - Next vertex matrix for path reconstruction
        """
        # Create copies of the matrices
        dist = [row[:] for row in self.dist]
        next = [row[:] for row in self.next]
        
        # Floyd-Warshall algorithm
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
                            next[i][j] = next[i][k]
                            
        # Check for negative cycles
        for i in range(self.V):
            if dist[i][i] < 0:
                raise ValueError("Graph contains a negative weight cycle")
                
        return dist, next
        
    def reconstruct_path(self, start: int, end: int, next: List[List[int]]) -> List[int]:
        """Reconstruct the shortest path from start to end"""
        if next[start][end] is None:
            return []
            
        path = [start]
        while start != end:
            start = next[start][end]
            path.append(start)
        return path
        
    def print_all_pairs_shortest_paths(self, dist: List[List[float]], next: List[List[int]]):
        """Print all pairs shortest paths and their distances"""
        print("\nAll Pairs Shortest Paths:")
        for i in range(self.V):
            for j in range(self.V):
                if i == j:
                    continue
                    
                if dist[i][j] == float('inf'):
                    print(f"No path exists from {i} to {j}")
                    continue
                    
                path = self.reconstruct_path(i, j, next)
                print(f"Path from {i} to {j}: {' -> '.join(map(str, path))} (Distance: {dist[i][j]})")

# Example usage
if __name__ == "__main__":
    # Test case 1: Simple graph with positive weights
    print("Test Case 1: Simple Graph with Positive Weights")
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
        
    dist, next = g1.floyd_warshall()
    g1.print_all_pairs_shortest_paths(dist, next)
    print("-" * 50)
    
    # Test case 2: Graph with negative weights but no negative cycles
    print("\nTest Case 2: Graph with Negative Weights (No Negative Cycles)")
    g2 = Graph(3)
    edges = [
        (0, 1, 4),
        (0, 2, -2),
        (1, 2, 3),
        (1, 0, -1),
        (2, 1, 1)
    ]
    
    for u, v, w in edges:
        g2.add_edge(u, v, w)
        
    dist, next = g2.floyd_warshall()
    g2.print_all_pairs_shortest_paths(dist, next)
    print("-" * 50)
    
    # Test case 3: Graph with negative cycle
    print("\nTest Case 3: Graph with Negative Cycle")
    g3 = Graph(3)
    edges = [
        (0, 1, 1),
        (1, 2, 2),
        (2, 0, -4)
    ]
    
    for u, v, w in edges:
        g3.add_edge(u, v, w)
        
    try:
        dist, next = g3.floyd_warshall()
        g3.print_all_pairs_shortest_paths(dist, next)
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 50) 