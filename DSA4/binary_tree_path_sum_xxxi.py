from typing import List, Optional, Dict, Tuple
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum_xxxi(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    Find all paths that sum to a given value using iterative DFS with path tracking and memoization.
    Paths can start and end at any node, not just downward.
    
    Args:
        root: Root node of the binary tree
        target_sum: Target sum to find in paths
        
    Returns:
        List of paths (each path is a list of node values)
    """
    if not root:
        return []
    
    result = []
    seen_paths = set()  # Track unique paths
    memo = defaultdict(int)  # Memoization for path sums
    
    # Stack elements: (node, current_path, prefix_sums, visited)
    stack = [(root, [], {0: 1}, False)]
    
    while stack:
        node, current_path, prefix_sums, visited = stack.pop()
        
        if visited:
            # Post-order processing
            current_path.pop()
            continue
        
        # Add current node to path
        current_path.append(node.val)
        
        # Calculate current sum
        current_sum = sum(current_path)
        
        # Check if we've found a path that sums to target
        if current_sum == target_sum:
            path_key = tuple(current_path)
            if path_key not in seen_paths:
                result.append(current_path.copy())
                seen_paths.add(path_key)
        
        # Check all possible subpaths ending at current node
        temp_sum = 0
        for i in range(len(current_path) - 1, -1, -1):
            temp_sum += current_path[i]
            if temp_sum == target_sum:
                path = current_path[i:]
                path_key = tuple(path)
                if path_key not in seen_paths:
                    result.append(path.copy())
                    seen_paths.add(path_key)
        
        # Push children to stack with post-order marker
        stack.append((node, current_path, prefix_sums, True))
        
        if node.right:
            new_prefix_sums = prefix_sums.copy()
            new_prefix_sums[current_sum] = new_prefix_sums.get(current_sum, 0) + 1
            stack.append((node.right, current_path.copy(), new_prefix_sums, False))
        
        if node.left:
            new_prefix_sums = prefix_sums.copy()
            new_prefix_sums[current_sum] = new_prefix_sums.get(current_sum, 0) + 1
            stack.append((node.left, current_path.copy(), new_prefix_sums, False))
    
    return result

def list_to_tree(lst: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Convert a list representation to a binary tree.
    The list is in level-order traversal (breadth-first) order.
    None values represent null nodes.
    """
    if not lst or lst[0] is None:
        return None
    
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while queue and i < len(lst):
        node = queue.pop(0)
        
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_path_sum_xxxi():
    """Test cases for the binary tree path sum XXXI solution."""
    
    test_cases = [
        # Basic cases
        (([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8), [[5, 3], [5, 2, 1], [-3, 11], [3, -2, 7]]),
        (([1, 2, 3], 3), [[1, 2], [3]]),
        (([1, 2], 3), [[1, 2]]),
        
        # Edge cases
        (([], 0), []),
        (([1], 1), [[1]]),
        (([1, 2, None], 3), [[1, 2]]),
        (([1, None, 2], 3), [[1, 2]]),
        
        # Complete binary tree
        (([1, 2, 3, 4, 5, 6, 7], 7), [[1, 2, 4], [3, 4], [7]]),
        (([1, 2, 3, 4, 5, 6, 7], 8), [[1, 2, 5], [1, 3, 4], [2, 6]]),
        
        # Left-skewed tree
        (([1, 2, None, 3, None, 4], 10), [[1, 2, 3, 4]]),
        
        # Right-skewed tree
        (([1, None, 2, None, None, None, 3], 6), [[1, 2, 3]]),
        
        # Complex cases
        (([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 18), [[5, 4, 11, -2], [5, 8, 4, 1], [4, 11, 3]]),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), [[1, 2, 4, 8], [1, 2, 5, 7], [1, 3, 6, 5], [4, 11], [15]]),
        
        # Large tree
        (list(range(1, 16)) + [None] * 15, 15), [[1, 2, 4, 8], [4, 11], [15]]),
        
        # Edge cases with None values
        (([1, None, 2, None, None, 3, None], 6), [[1, 2, 3]]),
        (([1, 2, None, 3, None, None, None], 6), [[1, 2, 3]]),
        
        # Mixed values
        (([10, 5, 15, 3, 7, 12, 20], 18), [[10, 5, 3], [3, 15]]),
        
        # All negative numbers
        (([-1, -2, -3, -4, -5], -6), [[-1, -2, -3], [-2, -4]]),
        
        # Single negative number
        (([-1], -1), [[-1]]),
        
        # Zero sum
        (([1, -1, 2, -2, 3, -3], 0), [[1, -1], [2, -2], [3, -3], [1, -1, 2, -2]]),
        
        # Multiple paths with same sum
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), [[1, 2, 3, 4], [1, 3, 6], [2, 8], [10]]),
        
        # Special case with overlapping paths
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 10), [[1, 2, 3, 4], [1, 3, 6], [2, 8], [10]]),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), [[1, 2, 4, 8], [1, 2, 5, 7], [1, 3, 6, 5], [4, 11], [15]])
    ]
    
    print("Testing Binary Tree Path Sum XXXI Solution...")
    for (tree_list, target), expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get paths with target sum
        result = path_sum_xxxi(root, target)
        
        print(f"\nInput: {tree_list}, Target: {target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_path_sum_xxxi() 