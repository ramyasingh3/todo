from typing import List, Set, Dict
from collections import defaultdict

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)
        self.reverse_graph = defaultdict(list)
        
    def add_edge(self, u: int, v: int):
        """Add a directed edge to the graph"""
        self.graph[u].append(v)
        self.reverse_graph[v].append(u)
        
    def dfs_first(self, vertex: int, visited: Set[int], order: List[int]):
        """First DFS to fill the order stack"""
        visited.add(vertex)
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_first(neighbor, visited, order)
                
        order.append(vertex)
        
    def dfs_second(self, vertex: int, visited: Set[int], component: List[int]):
        """Second DFS to find SCC"""
        visited.add(vertex)
        component.append(vertex)
        
        for neighbor in self.reverse_graph[vertex]:
            if neighbor not in visited:
                self.dfs_second(neighbor, visited, component)
                
    def kosaraju_scc(self) -> List[List[int]]:
        """
        Find all strongly connected components using Kosaraju's algorithm
        
        Returns:
            List[List[int]]: List of strongly connected components
        """
        # First DFS to fill the order stack
        visited = set()
        order = []
        
        for vertex in range(self.V):
            if vertex not in visited:
                self.dfs_first(vertex, visited, order)
                
        # Second DFS to find SCCs
        visited = set()
        sccs = []
        
        # Process vertices in reverse order
        for vertex in reversed(order):
            if vertex not in visited:
                component = []
                self.dfs_second(vertex, visited, component)
                sccs.append(component)
                
        return sccs
        
    def print_sccs(self, sccs: List[List[int]]):
        """Print the strongly connected components"""
        print("\nStrongly Connected Components:")
        for i, component in enumerate(sccs, 1):
            print(f"Component {i}: {component}")

# Example usage
if __name__ == "__main__":
    # Test case 1: Simple graph with multiple SCCs
    print("Test Case 1: Simple Graph with Multiple SCCs")
    g1 = Graph(5)
    edges = [
        (1, 0),
        (0, 2),
        (2, 1),
        (0, 3),
        (3, 4)
    ]
    
    for u, v in edges:
        g1.add_edge(u, v)
        
    sccs = g1.kosaraju_scc()
    g1.print_sccs(sccs)
    print("-" * 50)
    
    # Test case 2: Graph with one large SCC
    print("\nTest Case 2: Graph with One Large SCC")
    g2 = Graph(7)
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 0)
    ]
    
    for u, v in edges:
        g2.add_edge(u, v)
        
    sccs = g2.kosaraju_scc()
    g2.print_sccs(sccs)
    print("-" * 50)
    
    # Test case 3: Graph with isolated vertices
    print("\nTest Case 3: Graph with Isolated Vertices")
    g3 = Graph(6)
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (3, 4),
        (4, 3)
    ]
    
    for u, v in edges:
        g3.add_edge(u, v)
        
    sccs = g3.kosaraju_scc()
    g3.print_sccs(sccs)
    print("-" * 50)
    
    # Test case 4: Complex graph with multiple SCCs
    print("\nTest Case 4: Complex Graph with Multiple SCCs")
    g4 = Graph(8)
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (2, 4),
        (4, 5),
        (5, 6),
        (6, 4),
        (6, 7)
    ]
    
    for u, v in edges:
        g4.add_edge(u, v)
        
    sccs = g4.kosaraju_scc()
    g4.print_sccs(sccs)
    print("-" * 50) 