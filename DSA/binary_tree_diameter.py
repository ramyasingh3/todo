from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Find the diameter of a binary tree.
    The diameter is defined as the length of the longest path between any two nodes
    in a tree. This path may or may not pass through the root.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        Length of the longest path between any two nodes
    """
    diameter = 0
    
    def height(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not node:
            return 0
            
        # Get heights of left and right subtrees
        left_height = height(node.left)
        right_height = height(node.right)
        
        # Update diameter if current path is longer
        diameter = max(diameter, left_height + right_height)
        
        # Return height of current node
        return 1 + max(left_height, right_height)
    
    height(root)
    return diameter

def list_to_tree(lst: list) -> Optional[TreeNode]:
    """Convert a list representation to a binary tree."""
    if not lst:
        return None
        
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while queue and i < len(lst):
        node = queue.pop(0)
        
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_diameter():
    """Test cases for the binary tree diameter solution."""
    
    test_cases = [
        # Basic cases
        ([1, 2, 3, 4, 5], 3),  # Path: 4 -> 2 -> 1 -> 3 -> 5
        ([1], 0),
        ([], 0),
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], 4),  # Path: 4 -> 2 -> 1 -> 3 -> 7
        # Left skewed tree
        ([1, 2, None, 3, None, 4], 3),  # Path: 4 -> 3 -> 2 -> 1
        # Right skewed tree
        ([1, None, 2, None, 3, None, 4], 3),  # Path: 1 -> 2 -> 3 -> 4
        # Complex cases
        ([5, 3, 6, 2, 4, None, None, 1], 4),  # Path: 1 -> 2 -> 3 -> 4 -> 6
        # Large tree
        (list(range(1, 16)), 6),  # Path: 8 -> 4 -> 2 -> 1 -> 3 -> 7 -> 15
        # Edge cases
        ([1, None, None], 0),
        ([1, 2, None], 1),  # Path: 1 -> 2
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], 4),  # Path: 3 -> 5 -> 10 -> 15 -> 20
        # All negative numbers
        ([-1, -2, -3], 1),  # Path: -2 -> -1 -> -3
        # Single negative number
        ([-1], 0)
    ]
    
    print("Testing Binary Tree Diameter Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Calculate diameter
        result = diameter_of_binary_tree(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_diameter() 