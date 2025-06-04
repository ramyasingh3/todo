from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        """
        Get the right side view of a binary tree.
        
        Args:
            root (TreeNode): Root of the binary tree
            
        Returns:
            list: List of values visible from the right side
        """
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                
                # Only add the last node of each level
                if i == level_size - 1:
                    result.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result

def build_tree(values):
    """
    Build a binary tree from a list of values.
    None values represent empty nodes.
    """
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root

def print_tree(root, level=0, prefix="Root: "):
    """
    Print the binary tree in a readable format.
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Simple tree
    print("Test Case 1: Simple tree")
    tree1 = build_tree([1, 2, 3, None, 5, None, 4])
    print_tree(tree1)
    result1 = solution.rightSideView(tree1)
    print(f"Right side view: {result1}")
    print("Expected: [1, 3, 4]")
    print()
    
    # Test Case 2: Tree with only left children
    print("Test Case 2: Tree with only left children")
    tree2 = build_tree([1, 2, None, 3, None, 4, None])
    print_tree(tree2)
    result2 = solution.rightSideView(tree2)
    print(f"Right side view: {result2}")
    print("Expected: [1, 2, 3, 4]")
    print()
    
    # Test Case 3: Empty tree
    print("Test Case 3: Empty tree")
    tree3 = build_tree([])
    result3 = solution.rightSideView(tree3)
    print(f"Right side view: {result3}")
    print("Expected: []")
    print()
    
    # Test Case 4: Tree with only right children
    print("Test Case 4: Tree with only right children")
    tree4 = build_tree([1, None, 2, None, None, None, 3])
    print_tree(tree4)
    result4 = solution.rightSideView(tree4)
    print(f"Right side view: {result4}")
    print("Expected: [1, 2, 3]")
    print()
    
    # Test Case 5: Complex tree
    print("Test Case 5: Complex tree")
    tree5 = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print_tree(tree5)
    result5 = solution.rightSideView(tree5)
    print(f"Right side view: {result5}")
    print("Expected: [1, 3, 7, 15]") 