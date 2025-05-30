from typing import List, Tuple, Dict, Set
import heapq
from collections import defaultdict

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def add_edge(self, u: int, v: int, weight: int):
        """Add an undirected edge to the graph"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph
        
    def prim_mst(self) -> List[Tuple[int, int, int]]:
        """
        Find the Minimum Spanning Tree using Prim's algorithm
        
        Returns:
            List[Tuple[int, int, int]]: List of edges in the MST (weight, u, v)
        """
        # Initialize data structures
        visited = set()
        mst = []
        # Priority queue for edges (weight, u, v)
        pq = []
        
        # Start with vertex 0
        start_vertex = 0
        visited.add(start_vertex)
        
        # Add all edges from start vertex to priority queue
        for v, weight in self.graph[start_vertex]:
            heapq.heappush(pq, (weight, start_vertex, v))
            
        # Process edges until we have V-1 edges in MST
        while pq and len(mst) < self.V - 1:
            weight, u, v = heapq.heappop(pq)
            
            # Skip if both vertices are visited
            if v in visited:
                continue
                
            # Add edge to MST
            mst.append((weight, u, v))
            visited.add(v)
            
            # Add all edges from new vertex to priority queue
            for neighbor, weight in self.graph[v]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, v, neighbor))
                    
        return mst
        
    def print_mst(self, mst: List[Tuple[int, int, int]]):
        """Print the edges of the MST and total weight"""
        print("\nEdges in the Minimum Spanning Tree:")
        print("Edge\tWeight")
        total_weight = 0
        for weight, u, v in mst:
            print(f"{u} -- {v}\t{weight}")
            total_weight += weight
        print(f"\nTotal weight of MST: {total_weight}")

# Example usage
if __name__ == "__main__":
    # Test case 1: Simple graph
    print("Test Case 1: Simple Graph")
    g1 = Graph(4)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    for u, v, w in edges:
        g1.add_edge(u, v, w)
        
    mst = g1.prim_mst()
    g1.print_mst(mst)
    print("-" * 50)
    
    # Test case 2: Larger graph
    print("\nTest Case 2: Larger Graph")
    g2 = Graph(9)
    edges = [
        (0, 1, 4),
        (0, 7, 8),
        (1, 2, 8),
        (1, 7, 11),
        (2, 3, 7),
        (2, 8, 2),
        (2, 5, 4),
        (3, 4, 9),
        (3, 5, 14),
        (4, 5, 10),
        (5, 6, 2),
        (6, 7, 1),
        (6, 8, 6),
        (7, 8, 7)
    ]
    
    for u, v, w in edges:
        g2.add_edge(u, v, w)
        
    mst = g2.prim_mst()
    g2.print_mst(mst)
    print("-" * 50)
    
    # Test case 3: Disconnected graph
    print("\nTest Case 3: Disconnected Graph")
    g3 = Graph(6)
    edges = [
        (0, 1, 2),
        (1, 2, 3),
        (3, 4, 1),
        (4, 5, 2)
    ]
    
    for u, v, w in edges:
        g3.add_edge(u, v, w)
        
    mst = g3.prim_mst()
    g3.print_mst(mst)
    print("-" * 50) 