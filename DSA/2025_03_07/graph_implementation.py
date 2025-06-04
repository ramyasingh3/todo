from typing import Any, Dict, List, Set, Optional
from dataclasses import dataclass
from collections import deque

@dataclass
class Edge:
    """Edge class for Graph"""
    destination: Any
    weight: float = 1.0

class Graph:
    """Graph implementation using adjacency list"""
    
    def __init__(self, directed: bool = False):
        """
        Initialize graph
        
        Args:
            directed: Whether graph is directed
        """
        self.adjacency_list: Dict[Any, List[Edge]] = {}
        self.directed = directed
    
    def add_vertex(self, vertex: Any) -> None:
        """
        Add vertex to graph
        
        Args:
            vertex: Vertex to add
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, source: Any, destination: Any, weight: float = 1.0) -> None:
        """
        Add edge to graph
        
        Args:
            source: Source vertex
            destination: Destination vertex
            weight: Edge weight
        """
        if source not in self.adjacency_list:
            self.add_vertex(source)
        if destination not in self.adjacency_list:
            self.add_vertex(destination)
        
        self.adjacency_list[source].append(Edge(destination, weight))
        if not self.directed:
            self.adjacency_list[destination].append(Edge(source, weight))
    
    def remove_edge(self, source: Any, destination: Any) -> bool:
        """
        Remove edge from graph
        
        Args:
            source: Source vertex
            destination: Destination vertex
            
        Returns:
            True if edge was removed, False otherwise
        """
        if source not in self.adjacency_list or destination not in self.adjacency_list:
            return False
        
        # Remove edge from source to destination
        self.adjacency_list[source] = [
            edge for edge in self.adjacency_list[source]
            if edge.destination != destination
        ]
        
        # If undirected, also remove edge from destination to source
        if not self.directed:
            self.adjacency_list[destination] = [
                edge for edge in self.adjacency_list[destination]
                if edge.destination != source
            ]
        
        return True
    
    def remove_vertex(self, vertex: Any) -> bool:
        """
        Remove vertex from graph
        
        Args:
            vertex: Vertex to remove
            
        Returns:
            True if vertex was removed, False otherwise
        """
        if vertex not in self.adjacency_list:
            return False
        
        # Remove all edges to this vertex
        for v in self.adjacency_list:
            self.adjacency_list[v] = [
                edge for edge in self.adjacency_list[v]
                if edge.destination != vertex
            ]
        
        # Remove vertex
        del self.adjacency_list[vertex]
        return True
    
    def get_neighbors(self, vertex: Any) -> List[Any]:
        """
        Get neighbors of vertex
        
        Args:
            vertex: Vertex to get neighbors for
            
        Returns:
            List of neighbor vertices
        """
        if vertex not in self.adjacency_list:
            return []
        return [edge.destination for edge in self.adjacency_list[vertex]]
    
    def bfs(self, start: Any) -> List[Any]:
        """
        Perform breadth-first search
        
        Args:
            start: Starting vertex
            
        Returns:
            List of vertices in BFS order
        """
        if start not in self.adjacency_list:
            return []
        
        visited: Set[Any] = set()
        result: List[Any] = []
        queue = deque([start])
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(self.get_neighbors(vertex))
        
        return result
    
    def dfs(self, start: Any) -> List[Any]:
        """
        Perform depth-first search
        
        Args:
            start: Starting vertex
            
        Returns:
            List of vertices in DFS order
        """
        if start not in self.adjacency_list:
            return []
        
        visited: Set[Any] = set()
        result: List[Any] = []
        
        def dfs_helper(vertex: Any) -> None:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_helper(neighbor)
        
        dfs_helper(start)
        return result
    
    def has_cycle(self) -> bool:
        """
        Check if graph has cycle
        
        Returns:
            True if graph has cycle, False otherwise
        """
        visited: Set[Any] = set()
        recursion_stack: Set[Any] = set()
        
        def has_cycle_helper(vertex: Any) -> bool:
            visited.add(vertex)
            recursion_stack.add(vertex)
            
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    if has_cycle_helper(neighbor):
                        return True
                elif neighbor in recursion_stack:
                    return True
            
            recursion_stack.remove(vertex)
            return False
        
        for vertex in self.adjacency_list:
            if vertex not in visited:
                if has_cycle_helper(vertex):
                    return True
        
        return False

# Example usage
if __name__ == "__main__":
    # Create an undirected graph
    graph = Graph(directed=False)
    
    # Add vertices and edges
    print("Testing graph operations:")
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 1),
        ('B', 'C', 2),
        ('C', 'D', 3),
        ('D', 'E', 4),
        ('E', 'A', 5)
    ]
    
    for vertex in vertices:
        graph.add_vertex(vertex)
        print(f"Added vertex: {vertex}")
    
    for source, dest, weight in edges:
        graph.add_edge(source, dest, weight)
        print(f"Added edge: {source} -> {dest} (weight: {weight})")
    
    # Test BFS
    print("\nTesting BFS:")
    bfs_result = graph.bfs('A')
    print(f"BFS starting from A: {bfs_result}")
    
    # Test DFS
    print("\nTesting DFS:")
    dfs_result = graph.dfs('A')
    print(f"DFS starting from A: {dfs_result}")
    
    # Test cycle detection
    print("\nTesting cycle detection:")
    has_cycle = graph.has_cycle()
    print(f"Graph has cycle: {has_cycle}")
    
    # Test removing edge
    print("\nTesting edge removal:")
    removed = graph.remove_edge('A', 'B')
    print(f"Removed edge A-B: {removed}")
    
    # Test removing vertex
    print("\nTesting vertex removal:")
    removed = graph.remove_vertex('C')
    print(f"Removed vertex C: {removed}")
    
    # Test getting neighbors
    print("\nTesting getting neighbors:")
    for vertex in vertices:
        if vertex in graph.adjacency_list:
            neighbors = graph.get_neighbors(vertex)
            print(f"Neighbors of {vertex}: {neighbors}") 