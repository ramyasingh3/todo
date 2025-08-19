from typing import Any, Dict, List, Set, Optional
from dataclasses import dataclass
from collections import deque

@dataclass
class GraphNode:
    """Node class for Graph"""
    value: Any
    neighbors: Dict['GraphNode', int]  # neighbor -> weight

class Graph:
    """Graph implementation using adjacency list"""
    
    def __init__(self, directed: bool = False):
        """
        Initialize graph
        
        Args:
            directed: Whether graph is directed
        """
        self.nodes: Dict[Any, GraphNode] = {}
        self.directed = directed
    
    def add_node(self, value: Any) -> None:
        """
        Add node to graph
        
        Args:
            value: Value of node to add
        """
        if value not in self.nodes:
            self.nodes[value] = GraphNode(value, {})
    
    def add_edge(self, from_value: Any, to_value: Any, weight: int = 1) -> None:
        """
        Add edge to graph
        
        Args:
            from_value: Value of source node
            to_value: Value of destination node
            weight: Weight of edge
        """
        if from_value not in self.nodes:
            self.add_node(from_value)
        if to_value not in self.nodes:
            self.add_node(to_value)
        
        self.nodes[from_value].neighbors[self.nodes[to_value]] = weight
        if not self.directed:
            self.nodes[to_value].neighbors[self.nodes[from_value]] = weight
    
    def remove_edge(self, from_value: Any, to_value: Any) -> None:
        """
        Remove edge from graph
        
        Args:
            from_value: Value of source node
            to_value: Value of destination node
        """
        if from_value in self.nodes and to_value in self.nodes:
            from_node = self.nodes[from_value]
            to_node = self.nodes[to_value]
            
            if to_node in from_node.neighbors:
                del from_node.neighbors[to_node]
            
            if not self.directed and from_node in to_node.neighbors:
                del to_node.neighbors[from_node]
    
    def remove_node(self, value: Any) -> None:
        """
        Remove node from graph
        
        Args:
            value: Value of node to remove
        """
        if value in self.nodes:
            node = self.nodes[value]
            
            # Remove all edges to this node
            for other_node in self.nodes.values():
                if node in other_node.neighbors:
                    del other_node.neighbors[node]
            
            del self.nodes[value]
    
    def get_neighbors(self, value: Any) -> List[Any]:
        """
        Get neighbors of node
        
        Args:
            value: Value of node
            
        Returns:
            List of neighbor values
        """
        if value in self.nodes:
            return [neighbor.value for neighbor in self.nodes[value].neighbors]
        return []
    
    def get_edge_weight(self, from_value: Any, to_value: Any) -> Optional[int]:
        """
        Get weight of edge
        
        Args:
            from_value: Value of source node
            to_value: Value of destination node
            
        Returns:
            Weight of edge, or None if edge doesn't exist
        """
        if from_value in self.nodes and to_value in self.nodes:
            from_node = self.nodes[from_value]
            to_node = self.nodes[to_value]
            
            if to_node in from_node.neighbors:
                return from_node.neighbors[to_node]
        return None
    
    def bfs(self, start_value: Any) -> List[Any]:
        """
        Perform breadth-first search
        
        Args:
            start_value: Value of starting node
            
        Returns:
            List of values in BFS order
        """
        if start_value not in self.nodes:
            return []
        
        visited: Set[Any] = set()
        result: List[Any] = []
        queue = deque([start_value])
        visited.add(start_value)
        
        while queue:
            value = queue.popleft()
            result.append(value)
            
            for neighbor in self.get_neighbors(value):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start_value: Any) -> List[Any]:
        """
        Perform depth-first search
        
        Args:
            start_value: Value of starting node
            
        Returns:
            List of values in DFS order
        """
        if start_value not in self.nodes:
            return []
        
        visited: Set[Any] = set()
        result: List[Any] = []
        
        def dfs_helper(value: Any) -> None:
            visited.add(value)
            result.append(value)
            
            for neighbor in self.get_neighbors(value):
                if neighbor not in visited:
                    dfs_helper(neighbor)
        
        dfs_helper(start_value)
        return result

# Example usage
if __name__ == "__main__":
    # Create an undirected graph
    graph = Graph()
    
    # Add nodes
    print("Adding nodes:")
    for value in range(1, 7):
        graph.add_node(value)
        print(f"Added node: {value}")
    
    # Add edges
    print("\nAdding edges:")
    edges = [
        (1, 2, 1), (1, 3, 2),
        (2, 4, 3), (2, 5, 4),
        (3, 5, 5), (3, 6, 6),
        (4, 6, 7), (5, 6, 8)
    ]
    
    for from_val, to_val, weight in edges:
        graph.add_edge(from_val, to_val, weight)
        print(f"Added edge: {from_val} -> {to_val} (weight: {weight})")
    
    # Test get_neighbors
    print("\nTesting get_neighbors:")
    for value in range(1, 7):
        neighbors = graph.get_neighbors(value)
        print(f"Neighbors of {value}: {neighbors}")
    
    # Test get_edge_weight
    print("\nTesting get_edge_weight:")
    test_edges = [(1, 2), (2, 3), (4, 5)]
    for from_val, to_val in test_edges:
        weight = graph.get_edge_weight(from_val, to_val)
        print(f"Edge weight {from_val} -> {to_val}: {weight}")
    
    # Test BFS
    print("\nTesting BFS:")
    bfs_result = graph.bfs(1)
    print(f"BFS starting from 1: {bfs_result}")
    
    # Test DFS
    print("\nTesting DFS:")
    dfs_result = graph.dfs(1)
    print(f"DFS starting from 1: {dfs_result}")
    
    # Test remove_edge
    print("\nTesting remove_edge:")
    graph.remove_edge(1, 2)
    print("Removed edge: 1 -> 2")
    neighbors = graph.get_neighbors(1)
    print(f"Neighbors of 1: {neighbors}")
    
    # Test remove_node
    print("\nTesting remove_node:")
    graph.remove_node(3)
    print("Removed node: 3")
    for value in range(1, 7):
        if value != 3:
            neighbors = graph.get_neighbors(value)
            print(f"Neighbors of {value}: {neighbors}") 