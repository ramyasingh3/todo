from typing import Any, Optional, List
from dataclasses import dataclass

@dataclass
class TreeNode:
    """Node class for Binary Search Tree"""
    value: Any
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

class BinarySearchTree:
    """Binary Search Tree implementation"""
    
    def __init__(self):
        """Initialize empty BST"""
        self.root: Optional[TreeNode] = None
    
    def insert(self, value: Any) -> None:
        """
        Insert value into BST
        
        Args:
            value: Value to insert
        """
        if not self.root:
            self.root = TreeNode(value)
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    break
                current = current.right
    
    def search(self, value: Any) -> bool:
        """
        Search for value in BST
        
        Args:
            value: Value to search for
            
        Returns:
            True if value found, False otherwise
        """
        current = self.root
        while current:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    def inorder_traversal(self) -> List[Any]:
        """
        Perform inorder traversal of BST
        
        Returns:
            List of values in inorder traversal
        """
        result = []
        self._inorder_traversal_helper(self.root, result)
        return result
    
    def _inorder_traversal_helper(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper method for inorder traversal"""
        if node:
            self._inorder_traversal_helper(node.left, result)
            result.append(node.value)
            self._inorder_traversal_helper(node.right, result)
    
    def preorder_traversal(self) -> List[Any]:
        """
        Perform preorder traversal of BST
        
        Returns:
            List of values in preorder traversal
        """
        result = []
        self._preorder_traversal_helper(self.root, result)
        return result
    
    def _preorder_traversal_helper(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper method for preorder traversal"""
        if node:
            result.append(node.value)
            self._preorder_traversal_helper(node.left, result)
            self._preorder_traversal_helper(node.right, result)
    
    def postorder_traversal(self) -> List[Any]:
        """
        Perform postorder traversal of BST
        
        Returns:
            List of values in postorder traversal
        """
        result = []
        self._postorder_traversal_helper(self.root, result)
        return result
    
    def _postorder_traversal_helper(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper method for postorder traversal"""
        if node:
            self._postorder_traversal_helper(node.left, result)
            self._postorder_traversal_helper(node.right, result)
            result.append(node.value)

# Example usage
if __name__ == "__main__":
    # Create a BST
    bst = BinarySearchTree()
    
    # Test insert
    print("Testing insert:")
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        bst.insert(value)
        print(f"Inserted: {value}")
    
    # Test search
    print("\nTesting search:")
    search_values = [4, 9, 7]
    for value in search_values:
        found = bst.search(value)
        print(f"Searching for {value}: {'Found' if found else 'Not found'}")
    
    # Test traversals
    print("\nTesting traversals:")
    print(f"Inorder traversal: {bst.inorder_traversal()}")
    print(f"Preorder traversal: {bst.preorder_traversal()}")
    print(f"Postorder traversal: {bst.postorder_traversal()}") 