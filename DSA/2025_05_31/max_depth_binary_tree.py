class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    """
    Find the maximum depth of a binary tree.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        Maximum depth of the tree
        
    Example:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> max_depth(root)
        3
    """
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Test case 1:")
    print(f"Maximum depth: {max_depth(root1)}")
    
    # Test case 2: Empty tree
    root2 = None
    print("\nTest case 2:")
    print(f"Maximum depth: {max_depth(root2)}")
    
    # Test case 3: Single node
    root3 = TreeNode(1)
    print("\nTest case 3:")
    print(f"Maximum depth: {max_depth(root3)}")
    
    # Test case 4: Left-skewed tree
    root4 = TreeNode(1, TreeNode(2, TreeNode(3)))
    print("\nTest case 4:")
    print(f"Maximum depth: {max_depth(root4)}")
    
    # Test case 5: Right-skewed tree
    root5 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print("\nTest case 5:")
    print(f"Maximum depth: {max_depth(root5)}") 