class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Find the maximum path sum in a binary tree.
        A path is defined as any sequence of nodes from some starting node to any node
        in the tree along the parent-child connections. The path must contain at least one node.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            Maximum path sum
        """
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
                
            # Get maximum gains from left and right subtrees
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Calculate the price to start a new path where 'node' is the highest node
            price_newpath = node.value + left_gain + right_gain
            
            # Update the global maximum sum
            self.max_sum = max(self.max_sum, price_newpath)
            
            # Return the maximum gain if continue the same path
            return node.value + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

def build_test_tree1():
    """
    Builds test tree 1:
         1
        / \
       2   3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    return root

def build_test_tree2():
    """
    Builds test tree 2:
         -10
         /  \
        9   20
           /  \
          15   7
    """
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def build_test_tree3():
    """
    Builds test tree 3:
         -3
    """
    root = TreeNode(-3)
    return root

def print_tree(node, level=0, prefix="Root: "):
    """Helper function to print the tree structure"""
    if not node:
        return
    print("  " * level + prefix + str(node.value))
    if node.left or node.right:
        if node.left:
            print_tree(node.left, level + 1, "L--- ")
        if node.right:
            print_tree(node.right, level + 1, "R--- ")

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print("Test Case 1: Simple tree")
    root1 = build_test_tree1()
    print("Tree structure:")
    print_tree(root1)
    print(f"Maximum path sum: {solution.maxPathSum(root1)}")  # Expected: 6
    
    print("\nTest Case 2: Tree with negative values")
    root2 = build_test_tree2()
    print("Tree structure:")
    print_tree(root2)
    print(f"Maximum path sum: {solution.maxPathSum(root2)}")  # Expected: 42
    
    print("\nTest Case 3: Single node tree")
    root3 = build_test_tree3()
    print("Tree structure:")
    print_tree(root3)
    print(f"Maximum path sum: {solution.maxPathSum(root3)}")  # Expected: -3 