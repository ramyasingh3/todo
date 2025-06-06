# Dijkstra's Shortest Path Algorithm Implementation
# Time Complexity: O((V + E) log V) with binary heap, O(V²) with array
# Space Complexity: O(V)

import heapq
from collections import defaultdict
import sys

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v, weight):
        """Add a weighted edge from vertex u to vertex v"""
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
    
    def add_undirected_edge(self, u, v, weight):
        """Add an undirected weighted edge between vertices u and v"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
        self.vertices.add(u)
        self.vertices.add(v)

def dijkstra_basic(graph, start):
    """Basic Dijkstra's algorithm using array for min extraction"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()
    
    while len(visited) < len(graph):
        # Find vertex with minimum distance
        min_vertex = None
        min_distance = float('inf')
        
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex
        
        if min_vertex is None:
            break
        
        visited.add(min_vertex)
        
        # Update distances to neighbors
        for neighbor, weight in graph[min_vertex]:
            if neighbor not in visited:
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances

def dijkstra_heap(graph, start):
    """Dijkstra's algorithm using binary heap (priority queue)"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
    
    return distances

def dijkstra_with_path(graph, start, end):
    """Dijkstra's algorithm that returns shortest path"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        if current_vertex == end:
            break
        
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (new_distance, neighbor))
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    return distances[end] if distances[end] != float('inf') else -1, path

def dijkstra_all_paths(graph, start):
    """Dijkstra's algorithm that returns all shortest paths"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (new_distance, neighbor))
    
    # Reconstruct all paths
    paths = {}
    for vertex in graph:
        if distances[vertex] != float('inf'):
            path = []
            current = vertex
            while current is not None:
                path.append(current)
                current = previous[current]
            path.reverse()
            paths[vertex] = path
    
    return distances, paths

def dijkstra_multiple_sources(graph, sources):
    """Dijkstra's algorithm from multiple sources"""
    distances = {vertex: float('inf') for vertex in graph}
    pq = []
    
    # Initialize distances for source vertices
    for source in sources:
        distances[source] = 0
        pq.append((0, source))
    
    heapq.heapify(pq)
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
    
    return distances

def dijkstra_with_constraints(graph, start, max_weight):
    """Dijkstra's algorithm with maximum weight constraint"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in visited and weight <= max_weight:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
    
    return distances

def dijkstra_k_shortest_paths(graph, start, end, k):
    """Find k shortest paths using modified Dijkstra's algorithm"""
    if k == 1:
        distance, path = dijkstra_with_path(graph, start, end)
        return [(distance, path)] if distance != -1 else []
    
    # Use a priority queue to store k shortest paths
    pq = [(0, [start])]  # (total_distance, path)
    shortest_paths = []
    
    while pq and len(shortest_paths) < k:
        current_distance, current_path = heapq.heappop(pq)
        current_vertex = current_path[-1]
        
        if current_vertex == end:
            shortest_paths.append((current_distance, current_path))
            continue
        
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in current_path:  # Avoid cycles
                new_distance = current_distance + weight
                new_path = current_path + [neighbor]
                heapq.heappush(pq, (new_distance, new_path))
    
    return shortest_paths

def dijkstra_negative_weights(graph, start):
    """Modified Dijkstra's for graphs with negative weights (not recommended)"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Run V-1 iterations
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distances[vertex] != float('inf'):
                    new_distance = distances[vertex] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
    
    # Check for negative cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distances[vertex] != float('inf'):
                if distances[vertex] + weight < distances[neighbor]:
                    return None  # Negative cycle detected
    
    return distances

def dijkstra_visualization(graph, start):
    """Dijkstra's algorithm with step-by-step visualization"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    visited = set()
    step = 1
    
    print(f"Starting Dijkstra's algorithm from vertex {start}")
    print("=" * 50)
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        print(f"Step {step}: Processing vertex {current_vertex} (distance: {current_distance})")
        
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in visited:
                old_distance = distances[neighbor]
                new_distance = current_distance + weight
                
                if new_distance < old_distance:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
                    print(f"  Updated distance to {neighbor}: {old_distance} -> {new_distance}")
        
        print(f"  Current distances: {dict(distances)}")
        print()
        step += 1
    
    return distances

def dijkstra_comparison(graph, start):
    """Compare different Dijkstra implementations"""
    print("Dijkstra's Algorithm Comparison")
    print("=" * 50)
    
    import time
    
    # Test basic implementation
    start_time = time.time()
    distances_basic = dijkstra_basic(graph, start)
    basic_time = time.time() - start_time
    
    # Test heap implementation
    start_time = time.time()
    distances_heap = dijkstra_heap(graph, start)
    heap_time = time.time() - start_time
    
    print(f"Basic implementation time: {basic_time:.6f}s")
    print(f"Heap implementation time: {heap_time:.6f}s")
    print(f"Speedup: {basic_time / heap_time:.2f}x")
    print()
    
    # Verify results are the same
    results_match = all(distances_basic[v] == distances_heap[v] for v in graph)
    print(f"Results match: {results_match}")
    
    return distances_heap

# Example usage and testing
if __name__ == "__main__":
    print("Dijkstra's Shortest Path Algorithm Analysis")
    print("=" * 50)
    
    # Create sample weighted graph
    g = Graph()
    edges = [
        (0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5),
        (2, 3, 8), (2, 4, 10), (3, 4, 2), (3, 5, 6),
        (4, 5, 3)
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)
    
    print(f"Graph edges (u, v, weight): {edges}")
    print()
    
    start_vertex = 0
    
    # Test basic Dijkstra
    print("1. Basic Dijkstra's Algorithm:")
    distances_basic = dijkstra_basic(g.graph, start_vertex)
    for vertex, distance in sorted(distances_basic.items()):
        print(f"   Distance to {vertex}: {distance}")
    print()
    
    # Test heap-based Dijkstra
    print("2. Heap-based Dijkstra's Algorithm:")
    distances_heap = dijkstra_heap(g.graph, start_vertex)
    for vertex, distance in sorted(distances_heap.items()):
        print(f"   Distance to {vertex}: {distance}")
    print()
    
    # Test path finding
    print("3. Shortest Path Finding:")
    for end_vertex in range(1, 6):
        distance, path = dijkstra_with_path(g.graph, start_vertex, end_vertex)
        print(f"   Path to {end_vertex}: {path} (distance: {distance})")
    print()
    
    # Test all paths
    print("4. All Shortest Paths:")
    distances, paths = dijkstra_all_paths(g.graph, start_vertex)
    for vertex, path in paths.items():
        print(f"   Path to {vertex}: {path} (distance: {distances[vertex]})")
    print()
    
    # Test multiple sources
    print("5. Multiple Sources Dijkstra:")
    sources = [0, 2]
    multi_distances = dijkstra_multiple_sources(g.graph, sources)
    for vertex, distance in sorted(multi_distances.items()):
        print(f"   Distance to {vertex}: {distance}")
    print()
    
    # Test k shortest paths
    print("6. K Shortest Paths:")
    k_paths = dijkstra_k_shortest_paths(g.graph, 0, 5, 3)
    for i, (distance, path) in enumerate(k_paths, 1):
        print(f"   {i}nd shortest path: {path} (distance: {distance})")
    print()
    
    # Test with constraints
    print("7. Dijkstra with Weight Constraint (max weight = 3):")
    constrained_distances = dijkstra_with_constraints(g.graph, start_vertex, 3)
    for vertex, distance in sorted(constrained_distances.items()):
        print(f"   Distance to {vertex}: {distance}")
    print()
    
    # Performance comparison
    print("=" * 50)
    print("Performance Comparison:")
    
    # Create larger graph for testing
    large_g = Graph()
    import random
    
    for i in range(100):
        for j in range(i + 1, min(i + 10, 100)):
            weight = random.randint(1, 100)
            large_g.add_edge(i, j, weight)
    
    comparison_result = dijkstra_comparison(large_g.graph, 0)
    
    # Visualization example
    print("=" * 50)
    print("Step-by-step Visualization:")
    small_g = Graph()
    small_edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5), (2, 3, 8)]
    for u, v, w in small_edges:
        small_g.add_edge(u, v, w)
    
    dijkstra_visualization(small_g.graph, 0) 