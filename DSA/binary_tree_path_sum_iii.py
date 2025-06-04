from typing import List, Optional, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum_iii(root: Optional[TreeNode], target_sum: int) -> int:
    """
    Find the number of paths that sum to a given value.
    The path does not need to start or end at the root or a leaf, but it must go downwards.
    
    Args:
        root: Root node of the binary tree
        target_sum: Target sum to find in paths
        
    Returns:
        Number of paths that sum to target_sum
    """
    if not root:
        return 0
    
    # Dictionary to store prefix sums and their counts
    prefix_sums = {0: 1}
    count = 0
    
    def dfs(node: TreeNode, current_sum: int) -> None:
        nonlocal count
        if not node:
            return
        
        current_sum += node.val
        
        # Check if there's a prefix sum that can be subtracted to get target_sum
        count += prefix_sums.get(current_sum - target_sum, 0)
        
        # Update prefix sums
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
        # Continue DFS
        dfs(node.left, current_sum)
        dfs(node.right, current_sum)
        
        # Backtrack
        prefix_sums[current_sum] -= 1
        if prefix_sums[current_sum] == 0:
            del prefix_sums[current_sum]
    
    dfs(root, 0)
    return count

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

def test_path_sum_iii():
    """Test cases for the binary tree path sum III solution."""
    
    test_cases = [
        # Basic cases
        (([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8), 3),
        (([1, 2, 3], 3), 2),
        (([1, 2], 3), 1),
        
        # Edge cases
        (([], 0), 0),
        (([1], 1), 1),
        (([1, 2, None], 3), 1),
        (([1, None, 2], 3), 1),
        
        # Complete binary tree
        (([1, 2, 3, 4, 5, 6, 7], 7), 2),
        (([1, 2, 3, 4, 5, 6, 7], 8), 2),
        
        # Left-skewed tree
        (([1, 2, None, 3, None, 4], 10), 1),
        
        # Right-skewed tree
        (([1, None, 2, None, None, None, 3], 6), 1),
        
        # Complex cases
        (([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 18), 3),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 5),
        
        # Large tree
        (list(range(1, 16)) + [None] * 15, 15), 5),
        
        # Edge cases with None values
        (([1, None, 2, None, None, 3, None], 6), 1),
        (([1, 2, None, 3, None, None, None], 6), 1),
        
        # Mixed values
        (([10, 5, 15, 3, 7, 12, 20], 18), 3),
        
        # All negative numbers
        (([-1, -2, -3, -4, -5], -6), 1),
        
        # Single negative number
        (([-1], -1), 1),
        
        # Zero sum
        (([1, -1, 2, -2, 3, -3], 0), 3),
        
        # Multiple paths with same sum
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 4),
        
        # Special case with overlapping paths
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 10), 4),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 5)
    ]
    
    print("Testing Binary Tree Path Sum III Solution...")
    for (tree_list, target), expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get number of paths with target sum
        result = path_sum_iii(root, target)
        
        print(f"\nInput: {tree_list}, Target: {target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_path_sum_iii() 