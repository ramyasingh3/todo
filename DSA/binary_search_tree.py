class TreeNode:
    """Node class for Binary Search Tree"""
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation with basic operations"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, val: int) -> None:
        """Insert a value into the BST"""
        if not self.root:
            self.root = TreeNode(val)
            return
        
        def _insert(node: TreeNode, val: int) -> None:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    _insert(node.left, val)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    _insert(node.right, val)
        
        _insert(self.root, val)
    
    def search(self, val: int) -> bool:
        """Search for a value in the BST"""
        def _search(node: TreeNode, val: int) -> bool:
            if not node:
                return False
            if node.val == val:
                return True
            if val < node.val:
                return _search(node.left, val)
            return _search(node.right, val)
        
        return _search(self.root, val)
    
    def delete(self, val: int) -> None:
        """Delete a value from the BST"""
        def _find_min(node: TreeNode) -> TreeNode:
            current = node
            while current.left:
                current = current.left
            return current
        
        def _delete(node: TreeNode, val: int) -> TreeNode:
            if not node:
                return node
            
            if val < node.val:
                node.left = _delete(node.left, val)
            elif val > node.val:
                node.right = _delete(node.right, val)
            else:
                # Node with only one child or no child
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                # Node with two children
                temp = _find_min(node.right)
                node.val = temp.val
                node.right = _delete(node.right, temp.val)
            
            return node
        
        self.root = _delete(self.root, val)
    
    def inorder_traversal(self) -> list[int]:
        """Perform inorder traversal of the BST"""
        result = []
        
        def _inorder(node: TreeNode) -> None:
            if not node:
                return
            _inorder(node.left)
            result.append(node.val)
            _inorder(node.right)
        
        _inorder(self.root)
        return result
    
    def preorder_traversal(self) -> list[int]:
        """Perform preorder traversal of the BST"""
        result = []
        
        def _preorder(node: TreeNode) -> None:
            if not node:
                return
            result.append(node.val)
            _preorder(node.left)
            _preorder(node.right)
        
        _preorder(self.root)
        return result
    
    def postorder_traversal(self) -> list[int]:
        """Perform postorder traversal of the BST"""
        result = []
        
        def _postorder(node: TreeNode) -> None:
            if not node:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.val)
        
        _postorder(self.root)
        return result

# Example usage
if __name__ == "__main__":
    # Create a BST
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
        print(f"Inserted {val}")
    
    # Test traversals
    print("\nInorder traversal:", bst.inorder_traversal())
    print("Preorder traversal:", bst.preorder_traversal())
    print("Postorder traversal:", bst.postorder_traversal())
    
    # Test search
    search_values = [40, 90, 50, 25]
    print("\nSearch results:")
    for val in search_values:
        print(f"Searching for {val}: {'Found' if bst.search(val) else 'Not found'}")
    
    # Test deletion
    delete_values = [30, 70, 50]
    print("\nDeletion results:")
    for val in delete_values:
        bst.delete(val)
        print(f"Deleted {val}")
        print("Inorder traversal after deletion:", bst.inorder_traversal()) 