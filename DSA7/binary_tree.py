from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, val: int):
        """Insert a value into the binary tree"""
        if not self.root:
            self.root = TreeNode(val)
            return
            
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            
            if not node.left:
                node.left = TreeNode(val)
                return
            queue.append(node.left)
            
            if not node.right:
                node.right = TreeNode(val)
                return
            queue.append(node.right)
            
    def inorder_traversal(self) -> List[int]:
        """Perform inorder traversal (left -> root -> right)"""
        result = []
        
        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
            
        inorder(self.root)
        return result
        
    def preorder_traversal(self) -> List[int]:
        """Perform preorder traversal (root -> left -> right)"""
        result = []
        
        def preorder(node: Optional[TreeNode]):
            if not node:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
            
        preorder(self.root)
        return result
        
    def postorder_traversal(self) -> List[int]:
        """Perform postorder traversal (left -> right -> root)"""
        result = []
        
        def postorder(node: Optional[TreeNode]):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
            
        postorder(self.root)
        return result
        
    def level_order_traversal(self) -> List[int]:
        """Perform level order traversal (breadth-first)"""
        if not self.root:
            return []
            
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, None, 2, 3],
        [1, 2, 3, None, None, 4, 5],
        [1],
        []
    ]
    
    for values in test_cases:
        tree = BinaryTree()
        for val in values:
            if val is not None:
                tree.insert(val)
                
        print(f"Input values: {values}")
        print(f"Inorder traversal: {tree.inorder_traversal()}")
        print(f"Preorder traversal: {tree.preorder_traversal()}")
        print(f"Postorder traversal: {tree.postorder_traversal()}")
        print(f"Level order traversal: {tree.level_order_traversal()}")
        print("-" * 50) 