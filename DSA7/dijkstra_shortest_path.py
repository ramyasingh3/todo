from typing import Dict, List, Set, Tuple
import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u: int, v: int, weight: int):
        """Add a weighted edge to the graph"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph
        
    def dijkstra(self, start: int) -> Tuple[Dict[int, int], Dict[int, int]]:
        """
        Find shortest paths from start vertex to all other vertices using Dijkstra's algorithm
        
        Args:
            start (int): Starting vertex
            
        Returns:
            Tuple[Dict[int, int], Dict[int, int]]: (distances, previous vertices)
        """
        # Initialize distances and previous vertices
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        previous = {vertex: None for vertex in self.graph}
        
        # Priority queue for vertices to visit
        pq = [(0, start)]
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            # If we've found a better path, skip
            if current_distance > distances[current_vertex]:
                continue
                
            # Check all neighbors
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                # If we found a better path, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
                    
        return distances, previous
        
    def get_shortest_path(self, start: int, end: int) -> Tuple[List[int], int]:
        """
        Get the shortest path from start to end vertex
        
        Args:
            start (int): Starting vertex
            end (int): Ending vertex
            
        Returns:
            Tuple[List[int], int]: (path, total distance)
        """
        distances, previous = self.dijkstra(start)
        
        if distances[end] == float('infinity'):
            return [], float('infinity')
            
        # Reconstruct the path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
            
        return path[::-1], distances[end]

# Example usage
if __name__ == "__main__":
    # Test case 1: Simple graph
    print("Test Case 1: Simple Graph")
    g1 = Graph()
    edges = [
        (0, 1, 4),  # (u, v, weight)
        (0, 2, 2),
        (1, 2, 1),
        (1, 3, 5),
        (2, 3, 8),
        (2, 4, 10),
        (3, 4, 2),
        (3, 5, 6),
        (4, 5, 3)
    ]
    
    for u, v, w in edges:
        g1.add_edge(u, v, w)
        
    start, end = 0, 5
    path, distance = g1.get_shortest_path(start, end)
    print(f"Shortest path from {start} to {end}: {path}")
    print(f"Total distance: {distance}")
    print("-" * 50)
    
    # Test case 2: Graph with disconnected components
    print("\nTest Case 2: Disconnected Components")
    g2 = Graph()
    edges = [
        (0, 1, 1),
        (1, 2, 2),
        (2, 3, 3),
        (4, 5, 1),
        (5, 6, 2)
    ]
    
    for u, v, w in edges:
        g2.add_edge(u, v, w)
        
    start, end = 0, 6
    path, distance = g2.get_shortest_path(start, end)
    print(f"Shortest path from {start} to {end}: {path}")
    print(f"Total distance: {distance}")
    print("-" * 50)
    
    # Test case 3: Graph with negative weights (Dijkstra's limitation)
    print("\nTest Case 3: Graph with Negative Weights")
    g3 = Graph()
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, -1),
        (1, 3, 5),
        (2, 3, 8)
    ]
    
    for u, v, w in edges:
        g3.add_edge(u, v, w)
        
    start, end = 0, 3
    path, distance = g3.get_shortest_path(start, end)
    print(f"Shortest path from {start} to {end}: {path}")
    print(f"Total distance: {distance}")
    print("-" * 50) 