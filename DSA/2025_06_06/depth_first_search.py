# Depth First Search (DFS) Implementation
# Time Complexity: O(V + E) where V is vertices and E is edges
# Space Complexity: O(V) for recursion stack

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v"""
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
    
    def add_undirected_edge(self, u, v):
        """Add an undirected edge between vertices u and v"""
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.vertices.add(u)
        self.vertices.add(v)

def dfs_recursive(graph, start, visited=None):
    """Recursive DFS implementation"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result

def dfs_iterative(graph, start):
    """Iterative DFS implementation using stack"""
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add unvisited neighbors to stack (in reverse order for correct traversal)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

def dfs_with_path(graph, start, end):
    """DFS to find path from start to end vertex"""
    def dfs_path_helper(current, target, visited, path):
        visited.add(current)
        path.append(current)
        
        if current == target:
            return path[:]
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                result = dfs_path_helper(neighbor, target, visited, path)
                if result:
                    return result
        
        path.pop()
        return None
    
    return dfs_path_helper(start, end, set(), [])

def dfs_connected_components(graph):
    """Find all connected components using DFS"""
    visited = set()
    components = []
    
    def dfs_component(start):
        component = []
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                component.append(vertex)
                
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return component
    
    for vertex in graph:
        if vertex not in visited:
            components.append(dfs_component(vertex))
    
    return components

def dfs_topological_sort(graph):
    """Topological sort using DFS"""
    visited = set()
    temp_visited = set()
    result = []
    
    def dfs_topological(vertex):
        if vertex in temp_visited:
            raise ValueError("Graph contains cycle")
        
        if vertex in visited:
            return
        
        temp_visited.add(vertex)
        
        for neighbor in graph[vertex]:
            dfs_topological(neighbor)
        
        temp_visited.remove(vertex)
        visited.add(vertex)
        result.append(vertex)
    
    for vertex in graph:
        if vertex not in visited:
            dfs_topological(vertex)
    
    return result[::-1]  # Reverse to get topological order

def dfs_detect_cycle(graph):
    """Detect cycle in directed graph using DFS"""
    visited = set()
    rec_stack = set()
    
    def has_cycle(vertex):
        visited.add(vertex)
        rec_stack.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if has_cycle(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(vertex)
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if has_cycle(vertex):
                return True
    
    return False

def dfs_bipartite_check(graph):
    """Check if graph is bipartite using DFS"""
    color = {}
    
    def is_bipartite_dfs(vertex, current_color):
        if vertex in color:
            return color[vertex] == current_color
        
        color[vertex] = current_color
        
        for neighbor in graph[vertex]:
            if not is_bipartite_dfs(neighbor, 1 - current_color):
                return False
        
        return True
    
    for vertex in graph:
        if vertex not in color:
            if not is_bipartite_dfs(vertex, 0):
                return False
    
    return True

def dfs_bridge_detection(graph):
    """Find bridges in undirected graph using DFS"""
    visited = set()
    discovery_time = {}
    low_time = {}
    bridges = []
    time = 0
    
    def find_bridges(vertex, parent):
        nonlocal time
        visited.add(vertex)
        discovery_time[vertex] = time
        low_time[vertex] = time
        time += 1
        
        for neighbor in graph[vertex]:
            if neighbor == parent:
                continue
            
            if neighbor not in visited:
                find_bridges(neighbor, vertex)
                low_time[vertex] = min(low_time[vertex], low_time[neighbor])
                
                if low_time[neighbor] > discovery_time[vertex]:
                    bridges.append((vertex, neighbor))
            else:
                low_time[vertex] = min(low_time[vertex], discovery_time[neighbor])
    
    for vertex in graph:
        if vertex not in visited:
            find_bridges(vertex, None)
    
    return bridges

def dfs_articulation_points(graph):
    """Find articulation points in undirected graph using DFS"""
    visited = set()
    discovery_time = {}
    low_time = {}
    articulation_points = set()
    time = 0
    
    def find_articulation_points(vertex, parent, is_root=True):
        nonlocal time
        visited.add(vertex)
        discovery_time[vertex] = time
        low_time[vertex] = time
        time += 1
        
        children = 0
        
        for neighbor in graph[vertex]:
            if neighbor == parent:
                continue
            
            if neighbor not in visited:
                children += 1
                find_articulation_points(neighbor, vertex, False)
                low_time[vertex] = min(low_time[vertex], low_time[neighbor])
                
                if not is_root and low_time[neighbor] >= discovery_time[vertex]:
                    articulation_points.add(vertex)
            else:
                low_time[vertex] = min(low_time[vertex], discovery_time[neighbor])
        
        if is_root and children > 1:
            articulation_points.add(vertex)
    
    for vertex in graph:
        if vertex not in visited:
            find_articulation_points(vertex, None)
    
    return list(articulation_points)

def dfs_maze_solver(maze, start, end):
    """Solve maze using DFS"""
    rows, cols = len(maze), len(maze[0])
    visited = set()
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0
    
    def dfs_maze(x, y, path):
        if (x, y) == end:
            return path + [(x, y)]
        
        visited.add((x, y))
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                result = dfs_maze(new_x, new_y, path + [(x, y)])
                if result:
                    return result
        
        return None
    
    return dfs_maze(start[0], start[1], [])

def dfs_sudoku_solver(board):
    """Solve Sudoku using DFS backtracking"""
    def is_valid(board, row, col, num):
        # Check row
        for x in range(9):
            if board[row][x] == num:
                return False
        
        # Check column
        for x in range(9):
            if board[x][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        
        return True
    
    def solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if solve_sudoku(board):
                                return True
                            board[i][j] = 0
                    return False
        return True
    
    if solve_sudoku(board):
        return board
    return None

def dfs_n_queens(n):
    """Solve N-Queens problem using DFS backtracking"""
    def is_safe(board, row, col):
        # Check row
        for j in range(col):
            if board[row][j] == 1:
                return False
        
        # Check upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def solve_n_queens(board, col):
        if col >= n:
            return True
        
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve_n_queens(board, col + 1):
                    return True
                board[i][col] = 0
        
        return False
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0):
        return board
    return None

# Example usage and testing
if __name__ == "__main__":
    print("Depth First Search (DFS) Algorithm Analysis")
    print("=" * 50)
    
    # Create sample graph
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (4, 7), (5, 8), (6, 8)]
    
    for u, v in edges:
        g.add_edge(u, v)
    
    print(f"Graph edges: {edges}")
    print()
    
    # Test basic DFS
    print("1. Basic DFS Traversal:")
    print(f"   Recursive: {dfs_recursive(g.graph, 0)}")
    print(f"   Iterative: {dfs_iterative(g.graph, 0)}")
    print()
    
    # Test path finding
    print("2. Path Finding:")
    path = dfs_with_path(g.graph, 0, 8)
    print(f"   Path from 0 to 8: {path}")
    print()
    
    # Test connected components
    print("3. Connected Components:")
    components = dfs_connected_components(g.graph)
    print(f"   Components: {components}")
    print()
    
    # Test topological sort
    print("4. Topological Sort:")
    try:
        topo_order = dfs_topological_sort(g.graph)
        print(f"   Topological order: {topo_order}")
    except ValueError as e:
        print(f"   Error: {e}")
    print()
    
    # Test cycle detection
    print("5. Cycle Detection:")
    has_cycle = dfs_detect_cycle(g.graph)
    print(f"   Has cycle: {has_cycle}")
    print()
    
    # Test bipartite check
    print("6. Bipartite Check:")
    is_bipartite = dfs_bipartite_check(g.graph)
    print(f"   Is bipartite: {is_bipartite}")
    print()
    
    # Test maze solver
    print("7. Maze Solver:")
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    maze_path = dfs_maze_solver(maze, start, end)
    print(f"   Maze path: {maze_path}")
    print()
    
    # Test N-Queens
    print("8. N-Queens Solution:")
    n = 4
    queens_solution = dfs_n_queens(n)
    if queens_solution:
        print(f"   {n}-Queens solution found:")
        for row in queens_solution:
            print(f"   {row}")
    else:
        print(f"   No solution for {n}-Queens")
    print()
    
    # Performance comparison
    print("=" * 50)
    print("Performance Comparison:")
    
    import time
    
    # Create larger graph for testing
    large_g = Graph()
    for i in range(1000):
        for j in range(i + 1, min(i + 10, 1000)):
            large_g.add_edge(i, j)
    
    # Test recursive vs iterative
    start = time.time()
    dfs_recursive(large_g.graph, 0)
    recursive_time = time.time() - start
    
    start = time.time()
    dfs_iterative(large_g.graph, 0)
    iterative_time = time.time() - start
    
    print(f"Recursive DFS: {recursive_time:.6f}s")
    print(f"Iterative DFS: {iterative_time:.6f}s") 