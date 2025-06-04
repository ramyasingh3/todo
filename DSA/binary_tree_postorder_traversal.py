from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Perform postorder traversal of a binary tree.
    Postorder traversal: left -> right -> root
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of node values in postorder traversal order
    """
    result = []
    stack = []
    last_visited = None
    
    while root or stack:
        # Go to the leftmost node
        while root:
            stack.append(root)
            root = root.left
        
        # Get the top node from stack
        node = stack[-1]
        
        # If right child exists and hasn't been visited yet
        if node.right and node.right != last_visited:
            root = node.right
        else:
            # Process the node
            result.append(node.val)
            last_visited = stack.pop()
    
    return result

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

def test_postorder_traversal():
    """Test cases for the binary tree postorder traversal solution."""
    
    test_cases = [
        # Basic cases
        ([1, None, 2, 3], [3, 2, 1]),
        ([], []),
        ([1], [1]),
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], [4, 5, 2, 6, 7, 3, 1]),
        # Left skewed tree
        ([1, 2, None, 3, None, 4], [4, 3, 2, 1]),
        # Right skewed tree
        ([1, None, 2, None, 3, None, 4], [4, 3, 2, 1]),
        # Complex cases
        ([5, 3, 6, 2, 4, None, None, 1], [1, 2, 4, 3, 6, 5]),
        # Large tree
        (list(range(1, 16)), [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]),
        # Edge cases
        ([1, None, None], [1]),
        ([1, 2, None], [2, 1]),
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], [3, 7, 5, 12, 20, 15, 10])
    ]
    
    print("Testing Binary Tree Postorder Traversal Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get postorder traversal
        result = postorder_traversal(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_postorder_traversal() 