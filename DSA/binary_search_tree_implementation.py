from typing import Optional, List, Any
from dataclasses import dataclass

@dataclass
class Node:
    """Node class for Binary Search Tree"""
    value: Any
    left: Optional['Node'] = None
    right: Optional['Node'] = None

class BinarySearchTree:
    """Binary Search Tree implementation"""
    
    def __init__(self):
        self.root: Optional[Node] = None
    
    def insert(self, value: Any) -> None:
        """
        Insert a value into the BST
        
        Args:
            value: Value to be inserted
        """
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node: Node, value: Any) -> None:
        """Helper method for recursive insertion"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value: Any) -> bool:
        """
        Search for a value in the BST
        
        Args:
            value: Value to search for
            
        Returns:
            True if value is found, False otherwise
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node: Optional[Node], value: Any) -> bool:
        """Helper method for recursive search"""
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def inorder_traversal(self) -> List[Any]:
        """
        Perform inorder traversal of the BST
        
        Returns:
            List of values in inorder traversal
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[Node], result: List[Any]) -> None:
        """Helper method for recursive inorder traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> List[Any]:
        """
        Perform preorder traversal of the BST
        
        Returns:
            List of values in preorder traversal
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: Optional[Node], result: List[Any]) -> None:
        """Helper method for recursive preorder traversal"""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> List[Any]:
        """
        Perform postorder traversal of the BST
        
        Returns:
            List of values in postorder traversal
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: Optional[Node], result: List[Any]) -> None:
        """Helper method for recursive postorder traversal"""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

# Example usage
if __name__ == "__main__":
    # Create a BST
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    print("Inserting values:", values)
    for value in values:
        bst.insert(value)
    
    # Test search
    print("\nTesting search:")
    test_values = [40, 90, 50, 25]
    for value in test_values:
        print(f"Searching for {value}: {'Found' if bst.search(value) else 'Not found'}")
    
    # Test traversals
    print("\nTesting traversals:")
    print("Inorder traversal:", bst.inorder_traversal())
    print("Preorder traversal:", bst.preorder_traversal())
    print("Postorder traversal:", bst.postorder_traversal()) 