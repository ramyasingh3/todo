from collections import defaultdict, deque
from typing import List, Set, Dict

class Graph:
    """Graph implementation using adjacency list representation"""
    
    def __init__(self):
        self.graph: Dict[int, List[int]] = defaultdict(list)
    
    def add_edge(self, u: int, v: int) -> None:
        """
        Add an edge to the graph
        
        Args:
            u: Source vertex
            v: Destination vertex
        """
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
    
    def bfs(self, start: int) -> List[int]:
        """
        Perform Breadth-First Search starting from vertex 'start'
        
        Args:
            start: Starting vertex
            
        Returns:
            List of vertices in BFS order
        """
        if start not in self.graph:
            return []
        
        visited: Set[int] = set()
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
    
    def dfs(self, start: int) -> List[int]:
        """
        Perform Depth-First Search starting from vertex 'start'
        
        Args:
            start: Starting vertex
            
        Returns:
            List of vertices in DFS order
        """
        if start not in self.graph:
            return []
        
        visited: Set[int] = set()
        result = []
        
        def _dfs(vertex: int) -> None:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    _dfs(neighbor)
        
        _dfs(start)
        return result
    
    def has_cycle(self) -> bool:
        """
        Check if the graph contains a cycle
        
        Returns:
            True if cycle exists, False otherwise
        """
        visited: Set[int] = set()
        
        def _has_cycle(vertex: int, parent: int) -> bool:
            visited.add(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if _has_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if _has_cycle(vertex, -1):
                    return True
        
        return False
    
    def is_connected(self) -> bool:
        """
        Check if the graph is connected
        
        Returns:
            True if graph is connected, False otherwise
        """
        if not self.graph:
            return True
        
        start = next(iter(self.graph))
        visited = set(self.bfs(start))
        
        return len(visited) == len(self.graph)

# Example usage
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    
    # Add edges
    edges = [
        (0, 1), (0, 2), (1, 2), (1, 3),
        (2, 3), (3, 4), (4, 5), (5, 6)
    ]
    
    for u, v in edges:
        g.add_edge(u, v)
        print(f"Added edge: {u} - {v}")
    
    # Test BFS
    print("\nBFS traversal starting from vertex 0:")
    print(g.bfs(0))
    
    # Test DFS
    print("\nDFS traversal starting from vertex 0:")
    print(g.dfs(0))
    
    # Test cycle detection
    print("\nDoes the graph have a cycle?")
    print(g.has_cycle())
    
    # Test connectivity
    print("\nIs the graph connected?")
    print(g.is_connected())
    
    # Create a disconnected graph
    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(2, 3)
    
    print("\nTesting disconnected graph:")
    print("Is the graph connected?")
    print(g2.is_connected()) 