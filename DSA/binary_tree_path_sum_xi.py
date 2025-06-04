from typing import List, Optional, Dict
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum_xi(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    Find all paths that sum to a given value using DFS with memoization.
    Paths can start and end at any node, but must go downward.
    
    Args:
        root: Root node of the binary tree
        target_sum: Target sum to find in paths
        
    Returns:
        List of paths (each path is a list of node values)
    """
    if not root:
        return []
    
    result = []
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    
    def dfs(node: Optional[TreeNode], current_sum: int, current_path: List[int]) -> None:
        if not node:
            return
        
        current_sum += node.val
        current_path.append(node.val)
        
        # Check if there's a prefix sum that makes current_sum - prefix_sum = target_sum
        if (current_sum - target_sum) in prefix_sums:
            # Find all possible paths ending at current node
            temp_sum = current_sum
            temp_path = current_path.copy()
            while temp_path:
                if temp_sum == target_sum:
                    result.append(temp_path.copy())
                temp_sum -= temp_path[0]
                temp_path.pop(0)
        
        # Update prefix sums
        prefix_sums[current_sum] += 1
        
        # Recursively process children
        dfs(node.left, current_sum, current_path)
        dfs(node.right, current_sum, current_path)
        
        # Backtrack
        prefix_sums[current_sum] -= 1
        if prefix_sums[current_sum] == 0:
            del prefix_sums[current_sum]
        current_path.pop()
    
    dfs(root, 0, [])
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

def test_path_sum_xi():
    """Test cases for the binary tree path sum XI solution."""
    
    test_cases = [
        # Basic cases
        (([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8), [[5, 3], [5, 2, 1], [-3, 11]]),
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
    
    print("Testing Binary Tree Path Sum XI Solution...")
    for (tree_list, target), expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get paths with target sum
        result = path_sum_xi(root, target)
        
        print(f"\nInput: {tree_list}, Target: {target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_path_sum_xi() 