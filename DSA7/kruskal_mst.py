from typing import List, Tuple, Dict
from collections import defaultdict

class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, x: int) -> int:
        """Find the root of the set containing x"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
        
    def union(self, x: int, y: int):
        """Union the sets containing x and y"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
            
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.edges = []
        
    def add_edge(self, u: int, v: int, weight: int):
        """Add an undirected edge to the graph"""
        self.edges.append((weight, u, v))
        
    def kruskal_mst(self) -> List[Tuple[int, int, int]]:
        """
        Find the Minimum Spanning Tree using Kruskal's algorithm
        
        Returns:
            List[Tuple[int, int, int]]: List of edges in the MST (weight, u, v)
        """
        # Sort edges by weight
        self.edges.sort()
        
        # Initialize disjoint set
        ds = DisjointSet(self.V)
        
        # Initialize MST
        mst = []
        
        # Process edges in order of increasing weight
        for weight, u, v in self.edges:
            # If including this edge doesn't create a cycle
            if ds.find(u) != ds.find(v):
                mst.append((weight, u, v))
                ds.union(u, v)
                
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
        
    mst = g1.kruskal_mst()
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
        
    mst = g2.kruskal_mst()
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
        
    mst = g3.kruskal_mst()
    g3.print_mst(mst)
    print("-" * 50) 