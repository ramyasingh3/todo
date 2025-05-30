from typing import List, Dict, Tuple
from collections import defaultdict

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.edges = []
        
    def add_edge(self, u: int, v: int, weight: float):
        """Add a weighted directed edge to the graph"""
        self.edges.append((u, v, weight))
        
    def bellman_ford(self, source: int) -> Tuple[Dict[int, float], Dict[int, int]]:
        """
        Find shortest paths from source to all vertices using Bellman-Ford algorithm
        
        Args:
            source: Source vertex
            
        Returns:
            Tuple containing:
            - Dictionary of distances from source to each vertex
            - Dictionary of predecessors for each vertex in the shortest path
        """
        # Initialize distances and predecessors
        distances = {v: float('inf') for v in range(self.V)}
        predecessors = {v: None for v in range(self.V)}
        distances[source] = 0
        
        # Relax all edges V-1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
        
        # Check for negative weight cycles
        for u, v, weight in self.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")
                
        return distances, predecessors
        
    def print_shortest_paths(self, source: int, distances: Dict[int, float], predecessors: Dict[int, int]):
        """Print the shortest paths from source to all vertices"""
        print(f"\nShortest paths from vertex {source}:")
        for v in range(self.V):
            if v == source:
                continue
                
            if distances[v] == float('inf'):
                print(f"No path exists from {source} to {v}")
                continue
                
            # Reconstruct path
            path = []
            current = v
            while current is not None:
                path.append(current)
                current = predecessors[current]
            path.reverse()
            
            print(f"Path to {v}: {' -> '.join(map(str, path))} (Distance: {distances[v]})")

# Example usage
if __name__ == "__main__":
    # Test case 1: Simple graph with positive weights
    print("Test Case 1: Simple Graph with Positive Weights")
    g1 = Graph(5)
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 1),
        (1, 3, 5),
        (2, 3, 8),
        (2, 4, 10),
        (3, 4, 2),
        (4, 3, 1)
    ]
    
    for u, v, w in edges:
        g1.add_edge(u, v, w)
        
    distances, predecessors = g1.bellman_ford(0)
    g1.print_shortest_paths(0, distances, predecessors)
    print("-" * 50)
    
    # Test case 2: Graph with negative weights but no negative cycles
    print("\nTest Case 2: Graph with Negative Weights (No Negative Cycles)")
    g2 = Graph(4)
    edges = [
        (0, 1, 1),
        (0, 2, 4),
        (1, 2, -2),
        (1, 3, 2),
        (2, 3, 3)
    ]
    
    for u, v, w in edges:
        g2.add_edge(u, v, w)
        
    distances, predecessors = g2.bellman_ford(0)
    g2.print_shortest_paths(0, distances, predecessors)
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
        distances, predecessors = g3.bellman_ford(0)
        g3.print_shortest_paths(0, distances, predecessors)
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 50) 