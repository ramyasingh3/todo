from collections import defaultdict
from typing import List, Set

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u: int, v: int):
        """Add an edge to the graph"""
        self.graph[u].append(v)
        
    def dfs_recursive(self, start: int) -> List[int]:
        """
        Perform DFS traversal recursively starting from the given vertex
        
        Args:
            start (int): Starting vertex
            
        Returns:
            List[int]: DFS traversal order
        """
        visited = set()
        result = []
        
        def dfs_util(vertex: int):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_util(neighbor)
                    
        dfs_util(start)
        return result
        
    def dfs_iterative(self, start: int) -> List[int]:
        """
        Perform DFS traversal iteratively starting from the given vertex
        
        Args:
            start (int): Starting vertex
            
        Returns:
            List[int]: DFS traversal order
        """
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add neighbors in reverse order to maintain DFS order
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        
        return result

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (edges, start_vertex)
        ([(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)], 2),
        ([(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5)], 0),
        ([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)], 0),
        ([(0, 1), (0, 2), (1, 3), (2, 3)], 0),
        ([(0, 1), (1, 2), (2, 0)], 0)
    ]
    
    for edges, start in test_cases:
        g = Graph()
        for u, v in edges:
            g.add_edge(u, v)
            
        print(f"Graph edges: {edges}")
        print(f"Starting vertex: {start}")
        print(f"Recursive DFS: {g.dfs_recursive(start)}")
        print(f"Iterative DFS: {g.dfs_iterative(start)}")
        print("-" * 50) 