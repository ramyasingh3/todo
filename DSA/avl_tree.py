class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Height of the node (used for balancing)

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        """Get the height of a node"""
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        """Get the balance factor of a node"""
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        """Update the height of a node"""
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    def right_rotate(self, y):
        """
        Perform right rotation
             y                  x
            / \               /   \
           x   T3   -->     T1    y
          / \                     / \
         T1  T2                 T2  T3
        """
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def left_rotate(self, x):
        """
        Perform left rotation
            x                    y
           / \                 /   \
          T1  y     -->      x     T3
             / \            / \
            T2  T3        T1  T2
        """
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def insert(self, root, value):
        """Insert a value into the AVL tree"""
        # Perform normal BST insertion
        if not root:
            return AVLNode(value)
        
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            return root  # Duplicate values not allowed
        
        # Update height of current node
        self.update_height(root)
        
        # Get balance factor
        balance = self.balance_factor(root)
        
        # Left Left Case
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def insert_value(self, value):
        """Wrapper method to insert a value"""
        self.root = self.insert(self.root, value)
    
    def inorder_traversal(self, root, result=None):
        """Inorder traversal of the AVL tree"""
        if result is None:
            result = []
        
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.value)
            self.inorder_traversal(root.right, result)
        
        return result
    
    def print_tree(self, node, level=0, prefix="Root: "):
        """Print the tree structure"""
        if not node:
            return
        
        print("  " * level + prefix + f"{node.value} (h={node.height})")
        if node.left or node.right:
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")

# Test cases
if __name__ == "__main__":
    avl_tree = AVLTree()
    
    # Test case 1: Left-Left case
    print("\nTest Case 1: Left-Left Case")
    values1 = [30, 20, 10]
    for value in values1:
        avl_tree.insert_value(value)
    print("Tree after inserting", values1)
    avl_tree.print_tree(avl_tree.root)
    print("Inorder traversal:", avl_tree.inorder_traversal(avl_tree.root))
    
    # Test case 2: Right-Right case
    avl_tree = AVLTree()
    print("\nTest Case 2: Right-Right Case")
    values2 = [10, 20, 30]
    for value in values2:
        avl_tree.insert_value(value)
    print("Tree after inserting", values2)
    avl_tree.print_tree(avl_tree.root)
    print("Inorder traversal:", avl_tree.inorder_traversal(avl_tree.root))
    
    # Test case 3: Left-Right case
    avl_tree = AVLTree()
    print("\nTest Case 3: Left-Right Case")
    values3 = [30, 10, 20]
    for value in values3:
        avl_tree.insert_value(value)
    print("Tree after inserting", values3)
    avl_tree.print_tree(avl_tree.root)
    print("Inorder traversal:", avl_tree.inorder_traversal(avl_tree.root))
    
    # Test case 4: Complex insertions
    avl_tree = AVLTree()
    print("\nTest Case 4: Complex Insertions")
    values4 = [10, 20, 30, 40, 50, 25]
    for value in values4:
        avl_tree.insert_value(value)
    print("Tree after inserting", values4)
    avl_tree.print_tree(avl_tree.root)
    print("Inorder traversal:", avl_tree.inorder_traversal(avl_tree.root)) 