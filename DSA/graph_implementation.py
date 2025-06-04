from typing import List, Dict, Set, Optional, Tuple
from collections import deque, defaultdict

class Graph:
    """Graph implementation with both adjacency list and matrix representations"""
    
    def __init__(self, directed: bool = False):
        """
        Initialize Graph
        
        Args:
            directed: Whether the graph is directed
        """
        self.directed = directed
        self.adj_list: Dict[int, List[int]] = defaultdict(list)
        self.vertices: Set[int] = set()
        self.edge_count = 0
    
    def add_vertex(self, vertex: int) -> None:
        """
        Add a vertex to the graph
        
        Args:
            vertex: Vertex to add
        """
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            self.adj_list[vertex] = []
    
    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        Add an edge to the graph
        
        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex
        """
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        self.adj_list[from_vertex].append(to_vertex)
        if not self.directed:
            self.adj_list[to_vertex].append(from_vertex)
        
        self.edge_count += 1
    
    def get_adjacency_matrix(self) -> List[List[int]]:
        """
        Get adjacency matrix representation of the graph
        
        Returns:
            2D list representing adjacency matrix
        """
        if not self.vertices:
            return []
        
        # Create vertex to index mapping
        vertex_to_index = {v: i for i, v in enumerate(sorted(self.vertices))}
        size = len(self.vertices)
        
        # Initialize matrix with zeros
        matrix = [[0] * size for _ in range(size)]
        
        # Fill matrix
        for vertex, neighbors in self.adj_list.items():
            i = vertex_to_index[vertex]
            for neighbor in neighbors:
                j = vertex_to_index[neighbor]
                matrix[i][j] = 1
        
        return matrix
    
    def bfs(self, start_vertex: int) -> List[int]:
        """
        Perform Breadth-First Search starting from given vertex
        
        Args:
            start_vertex: Starting vertex for BFS
            
        Returns:
            List of vertices in BFS order
        """
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start_vertex: int) -> List[int]:
        """
        Perform Depth-First Search starting from given vertex
        
        Args:
            start_vertex: Starting vertex for DFS
            
        Returns:
            List of vertices in DFS order
        """
        if start_vertex not in self.vertices:
            return []
        
        visited = set()
        result = []
        
        def dfs_recursive(vertex: int) -> None:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_vertex)
        return result
    
    def has_cycle(self) -> bool:
        """
        Check if the graph has a cycle
        
        Returns:
            True if graph has a cycle, False otherwise
        """
        visited = set()
        rec_stack = set()
        
        def has_cycle_recursive(vertex: int) -> bool:
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    if has_cycle_recursive(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if has_cycle_recursive(vertex):
                    return True
        
        return False
    
    def get_vertex_count(self) -> int:
        """Get number of vertices in the graph"""
        return len(self.vertices)
    
    def get_edge_count(self) -> int:
        """Get number of edges in the graph"""
        return self.edge_count

# Example usage
if __name__ == "__main__":
    # Create an undirected graph
    graph = Graph(directed=False)
    
    # Add edges
    edges = [
        (0, 1), (0, 2), (1, 2), (1, 3),
        (2, 3), (3, 4), (4, 5), (5, 6)
    ]
    
    print("Adding edges:", edges)
    for from_vertex, to_vertex in edges:
        graph.add_edge(from_vertex, to_vertex)
    
    # Print graph information
    print(f"\nGraph has {graph.get_vertex_count()} vertices and {graph.get_edge_count()} edges")
    
    # Test BFS
    print("\nBFS starting from vertex 0:")
    print(graph.bfs(0))
    
    # Test DFS
    print("\nDFS starting from vertex 0:")
    print(graph.dfs(0))
    
    # Test cycle detection
    print(f"\nGraph has cycle: {graph.has_cycle()}")
    
    # Print adjacency matrix
    print("\nAdjacency Matrix:")
    matrix = graph.get_adjacency_matrix()
    for row in matrix:
        print(row)
    
    # Create a directed graph with cycle
    directed_graph = Graph(directed=True)
    cycle_edges = [(0, 1), (1, 2), (2, 0)]
    
    print("\nCreating directed graph with cycle:", cycle_edges)
    for from_vertex, to_vertex in cycle_edges:
        directed_graph.add_edge(from_vertex, to_vertex)
    
    print(f"Directed graph has cycle: {directed_graph.has_cycle()}") 