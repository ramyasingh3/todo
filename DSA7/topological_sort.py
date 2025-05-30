from typing import List, Set, Dict
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)
        self.in_degree = [0] * vertices
        
    def add_edge(self, u: int, v: int):
        """Add a directed edge to the graph"""
        self.graph[u].append(v)
        self.in_degree[v] += 1
        
    def topological_sort_dfs(self) -> List[int]:
        """
        Find topological order using DFS approach
        
        Returns:
            List[int]: Topological order of vertices
        """
        visited = set()
        temp = set()  # For cycle detection
        order = []
        
        def dfs(vertex: int) -> bool:
            """DFS helper function with cycle detection"""
            if vertex in temp:
                return False  # Cycle detected
            if vertex in visited:
                return True
                
            temp.add(vertex)
            
            for neighbor in self.graph[vertex]:
                if not dfs(neighbor):
                    return False
                    
            temp.remove(vertex)
            visited.add(vertex)
            order.append(vertex)
            return True
            
        # Try DFS from each unvisited vertex
        for vertex in range(self.V):
            if vertex not in visited:
                if not dfs(vertex):
                    return []  # Cycle detected, no valid topological order
                    
        return order[::-1]  # Reverse to get correct order
        
    def topological_sort_kahn(self) -> List[int]:
        """
        Find topological order using Kahn's algorithm (BFS approach)
        
        Returns:
            List[int]: Topological order of vertices
        """
        # Initialize queue with vertices having no incoming edges
        queue = deque([v for v in range(self.V) if self.in_degree[v] == 0])
        order = []
        
        # Process vertices in topological order
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            
            # Reduce in-degree of neighbors
            for neighbor in self.graph[vertex]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Check if we have a valid topological order
        return order if len(order) == self.V else []
        
    def print_order(self, order: List[int], algorithm: str):
        """Print the topological order"""
        if not order:
            print(f"\n{algorithm} - No valid topological order exists (cycle detected)")
        else:
            print(f"\n{algorithm} - Topological order: {order}")

# Example usage
if __name__ == "__main__":
    # Test case 1: Simple DAG
    print("Test Case 1: Simple DAG")
    g1 = Graph(6)
    edges = [
        (5, 2),
        (5, 0),
        (4, 0),
        (4, 1),
        (2, 3),
        (3, 1)
    ]
    
    for u, v in edges:
        g1.add_edge(u, v)
        
    # Test both algorithms
    order_dfs = g1.topological_sort_dfs()
    g1.print_order(order_dfs, "DFS")
    
    order_kahn = g1.topological_sort_kahn()
    g1.print_order(order_kahn, "Kahn's")
    print("-" * 50)
    
    # Test case 2: DAG with multiple valid orders
    print("\nTest Case 2: DAG with Multiple Valid Orders")
    g2 = Graph(7)
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 3),
        (3, 4),
        (3, 5),
        (4, 6),
        (5, 6)
    ]
    
    for u, v in edges:
        g2.add_edge(u, v)
        
    order_dfs = g2.topological_sort_dfs()
    g2.print_order(order_dfs, "DFS")
    
    order_kahn = g2.topological_sort_kahn()
    g2.print_order(order_kahn, "Kahn's")
    print("-" * 50)
    
    # Test case 3: Graph with cycle
    print("\nTest Case 3: Graph with Cycle")
    g3 = Graph(4)
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 1)  # Creates a cycle
    ]
    
    for u, v in edges:
        g3.add_edge(u, v)
        
    order_dfs = g3.topological_sort_dfs()
    g3.print_order(order_dfs, "DFS")
    
    order_kahn = g3.topological_sort_kahn()
    g3.print_order(order_kahn, "Kahn's")
    print("-" * 50) 