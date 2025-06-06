# Breadth First Search (BFS) Implementation
# Time Complexity: O(V + E) where V is vertices and E is edges
# Space Complexity: O(V) for queue

from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v, weight=1):
        """Add an edge from vertex u to vertex v with optional weight"""
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
    
    def add_undirected_edge(self, u, v, weight=1):
        """Add an undirected edge between vertices u and v"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
        self.vertices.add(u)
        self.vertices.add(v)

def bfs_basic(graph, start):
    """Basic BFS implementation"""
    visited = set()
    queue = deque([start])
    result = []
    
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor, _ in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def bfs_with_levels(graph, start):
    """BFS with level information"""
    visited = set()
    queue = deque([(start, 0)])  # (vertex, level)
    levels = defaultdict(list)
    
    visited.add(start)
    
    while queue:
        vertex, level = queue.popleft()
        levels[level].append(vertex)
        
        for neighbor, _ in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
    
    return dict(levels)

def bfs_shortest_path(graph, start, end):
    """Find shortest path using BFS"""
    if start == end:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])  # (vertex, path)
    
    visited.add(start)
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor, _ in graph[vertex]:
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

def bfs_shortest_path_unweighted(graph, start):
    """Find shortest paths from start to all vertices in unweighted graph"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        
        for neighbor, _ in graph[vertex]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    
    return distances

def bfs_connected_components(graph):
    """Find all connected components using BFS"""
    visited = set()
    components = []
    
    def bfs_component(start):
        component = []
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            component.append(vertex)
            
            for neighbor, _ in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return component
    
    for vertex in graph:
        if vertex not in visited:
            components.append(bfs_component(vertex))
    
    return components

def bfs_bipartite_check(graph):
    """Check if graph is bipartite using BFS"""
    color = {}
    
    for start in graph:
        if start in color:
            continue
        
        queue = deque([start])
        color[start] = 0
        
        while queue:
            vertex = queue.popleft()
            
            for neighbor, _ in graph[vertex]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[vertex]
                    queue.append(neighbor)
                elif color[neighbor] == color[vertex]:
                    return False
    
    return True

def bfs_cycle_detection_undirected(graph):
    """Detect cycle in undirected graph using BFS"""
    visited = set()
    
    def has_cycle_bfs(start):
        queue = deque([(start, None)])  # (vertex, parent)
        visited.add(start)
        
        while queue:
            vertex, parent = queue.popleft()
            
            for neighbor, _ in graph[vertex]:
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return True
                
                visited.add(neighbor)
                queue.append((neighbor, vertex))
        
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if has_cycle_bfs(vertex):
                return True
    
    return False

def bfs_maze_solver(maze, start, end):
    """Solve maze using BFS (guarantees shortest path)"""
    rows, cols = len(maze), len(maze[0])
    visited = set()
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0
    
    queue = deque([(start[0], start[1], [start])])  # (x, y, path)
    visited.add(start)
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y, path = queue.popleft()
        
        if (x, y) == end:
            return path
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, path + [(new_x, new_y)]))
    
    return None

def bfs_word_ladder(begin_word, end_word, word_list):
    """Word Ladder problem using BFS"""
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])  # (word, steps)
    visited = {begin_word}
    
    while queue:
        word, steps = queue.popleft()
        
        if word == end_word:
            return steps
        
        # Generate all possible one-letter transformations
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    
    return 0

def bfs_surrounded_regions(board):
    """Surrounded Regions problem using BFS"""
    if not board:
        return
    
    rows, cols = len(board), len(board[0])
    
    def bfs_flip(x, y):
        queue = deque([(x, y)])
        board[x][y] = 'T'  # Mark as temporary
        
        while queue:
            r, c = queue.popleft()
            
            # Check all four directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r + dr, c + dc
                
                if (0 <= new_r < rows and 0 <= new_c < cols and 
                    board[new_r][new_c] == 'O'):
                    board[new_r][new_c] = 'T'
                    queue.append((new_r, new_c))
    
    # Mark all 'O's connected to borders as 'T'
    for i in range(rows):
        for j in range(cols):
            if (board[i][j] == 'O' and 
                (i == 0 or i == rows - 1 or j == 0 or j == cols - 1)):
                bfs_flip(i, j)
    
    # Flip remaining 'O's to 'X' and 'T's back to 'O'
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'O'

def bfs_number_of_islands(grid):
    """Number of Islands problem using BFS"""
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def bfs_island(x, y):
        queue = deque([(x, y)])
        grid[x][y] = '0'  # Mark as visited
        
        while queue:
            r, c = queue.popleft()
            
            # Check all four directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = r + dr, c + dc
                
                if (0 <= new_r < rows and 0 <= new_c < cols and 
                    grid[new_r][new_c] == '1'):
                    grid[new_r][new_c] = '0'
                    queue.append((new_r, new_c))
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                bfs_island(i, j)
                count += 1
    
    return count

def bfs_rotting_oranges(grid):
    """Rotting Oranges problem using BFS"""
    if not grid:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    # Find all rotten oranges and count fresh ones
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
            elif grid[i][j] == 1:
                fresh += 1
    
    if fresh == 0:
        return 0
    
    max_time = 0
    
    while queue:
        r, c, time = queue.popleft()
        
        # Check all four directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r + dr, c + dc
            
            if (0 <= new_r < rows and 0 <= new_c < cols and 
                grid[new_r][new_c] == 1):
                grid[new_r][new_c] = 2
                fresh -= 1
                queue.append((new_r, new_c, time + 1))
                max_time = max(max_time, time + 1)
    
    return max_time if fresh == 0 else -1

def bfs_knight_moves(n, start, end):
    """Knight's shortest path on chessboard using BFS"""
    if start == end:
        return 0
    
    queue = deque([(start[0], start[1], 0)])  # (row, col, moves)
    visited = {start}
    
    # All possible knight moves
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    while queue:
        row, col, moves = queue.popleft()
        
        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 0 <= new_col < n and 
                (new_row, new_col) not in visited):
                
                if (new_row, new_col) == end:
                    return moves + 1
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, moves + 1))
    
    return -1

# Example usage and testing
if __name__ == "__main__":
    print("Breadth First Search (BFS) Algorithm Analysis")
    print("=" * 50)
    
    # Create sample graph
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (4, 7), (5, 8), (6, 8)]
    
    for u, v in edges:
        g.add_edge(u, v)
    
    print(f"Graph edges: {edges}")
    print()
    
    # Test basic BFS
    print("1. Basic BFS Traversal:")
    bfs_result = bfs_basic(g.graph, 0)
    print(f"   BFS traversal: {bfs_result}")
    print()
    
    # Test BFS with levels
    print("2. BFS with Levels:")
    levels = bfs_with_levels(g.graph, 0)
    for level, vertices in levels.items():
        print(f"   Level {level}: {vertices}")
    print()
    
    # Test shortest path
    print("3. Shortest Path:")
    path = bfs_shortest_path(g.graph, 0, 8)
    print(f"   Shortest path from 0 to 8: {path}")
    print()
    
    # Test shortest distances
    print("4. Shortest Distances:")
    distances = bfs_shortest_path_unweighted(g.graph, 0)
    for vertex, distance in sorted(distances.items()):
        print(f"   Distance to {vertex}: {distance}")
    print()
    
    # Test connected components
    print("5. Connected Components:")
    components = bfs_connected_components(g.graph)
    print(f"   Components: {components}")
    print()
    
    # Test bipartite check
    print("6. Bipartite Check:")
    is_bipartite = bfs_bipartite_check(g.graph)
    print(f"   Is bipartite: {is_bipartite}")
    print()
    
    # Test cycle detection
    print("7. Cycle Detection (Undirected):")
    has_cycle = bfs_cycle_detection_undirected(g.graph)
    print(f"   Has cycle: {has_cycle}")
    print()
    
    # Test maze solver
    print("8. Maze Solver (BFS - shortest path):")
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    maze_path = bfs_maze_solver(maze, start, end)
    print(f"   Shortest maze path: {maze_path}")
    print(f"   Path length: {len(maze_path) if maze_path else 0}")
    print()
    
    # Test word ladder
    print("9. Word Ladder:")
    begin = "hit"
    end = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    ladder_steps = bfs_word_ladder(begin, end, word_list)
    print(f"   Steps from '{begin}' to '{end}': {ladder_steps}")
    print()
    
    # Test knight moves
    print("10. Knight's Shortest Path:")
    n = 8
    start_pos = (0, 0)
    end_pos = (7, 7)
    knight_moves = bfs_knight_moves(n, start_pos, end_pos)
    print(f"   Knight moves from {start_pos} to {end_pos}: {knight_moves}")
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
    
    # Test BFS performance
    start = time.time()
    bfs_basic(large_g.graph, 0)
    bfs_time = time.time() - start
    
    print(f"BFS traversal time: {bfs_time:.6f}s")
    
    # Test shortest path performance
    start = time.time()
    bfs_shortest_path_unweighted(large_g.graph, 0)
    shortest_time = time.time() - start
    
    print(f"Shortest path calculation time: {shortest_time:.6f}s") 