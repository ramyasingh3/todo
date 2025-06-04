from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Find the lowest common ancestor (LCA) of two nodes in a binary tree.
    The lowest common ancestor is defined between two nodes p and q as the lowest node
    in the tree that has both p and q as descendants (where we allow a node to be a
    descendant of itself).
    
    Args:
        root: Root node of the binary tree
        p: First node
        q: Second node
        
    Returns:
        Lowest common ancestor node of p and q
    """
    if not root or root == p or root == q:
        return root
    
    # Search for p and q in left and right subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    # If both subtrees return non-null, current node is LCA
    if left and right:
        return root
    
    # Otherwise return the non-null subtree result
    return left if left else right

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

def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Find a node with the given value in the tree."""
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

def test_lowest_common_ancestor():
    """Test cases for the binary tree lowest common ancestor solution."""
    
    test_cases = [
        # Basic cases
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),  # LCA of 5 and 1 is 3
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),  # LCA of 5 and 4 is 5
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], 4, 5, 2),  # LCA of 4 and 5 is 2
        ([1, 2, 3, 4, 5, 6, 7], 6, 7, 3),  # LCA of 6 and 7 is 3
        # Left skewed tree
        ([1, 2, None, 3, None, 4], 2, 4, 2),  # LCA of 2 and 4 is 2
        # Right skewed tree
        ([1, None, 2, None, 3, None, 4], 2, 4, 2),  # LCA of 2 and 4 is 2
        # Complex cases
        ([5, 3, 6, 2, 4, None, None, 1], 1, 4, 3),  # LCA of 1 and 4 is 3
        # Large tree
        (list(range(1, 16)), 8, 9, 4),  # LCA of 8 and 9 is 4
        # Edge cases
        ([1, None, None], 1, 1, 1),  # LCA of 1 and 1 is 1
        ([1, 2, None], 1, 2, 1),  # LCA of 1 and 2 is 1
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], 3, 7, 5),  # LCA of 3 and 7 is 5
        # All negative numbers
        ([-1, -2, -3], -2, -3, -1),  # LCA of -2 and -3 is -1
        # Single negative number
        ([-1], -1, -1, -1)  # LCA of -1 and -1 is -1
    ]
    
    print("Testing Binary Tree Lowest Common Ancestor Solution...")
    for tree_list, p_val, q_val, expected_val in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Find nodes p and q
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        
        # Find LCA
        result = lowest_common_ancestor(root, p, q)
        
        print(f"\nInput: {tree_list}")
        print(f"Nodes: {p_val} and {q_val}")
        print(f"Expected LCA: {expected_val}")
        print(f"Got LCA: {result.val if result else None}")
        print(f"Test {'passed' if result and result.val == expected_val else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_lowest_common_ancestor() 