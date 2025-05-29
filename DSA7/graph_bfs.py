from collections import defaultdict, deque
from typing import List, Dict, Set

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u: int, v: int):
        """Add an edge to the graph"""
        self.graph[u].append(v)
        
    def bfs(self, start: int) -> List[int]:
        """
        Perform BFS traversal starting from the given vertex
        
        Args:
            start (int): Starting vertex
            
        Returns:
            List[int]: BFS traversal order
        """
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
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
        print(f"BFS traversal: {g.bfs(start)}")
        print("-" * 50) 