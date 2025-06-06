# Binary Search Tree Traversal Implementation
# Time Complexity: O(n) for all traversals where n is number of nodes
# Space Complexity: O(h) where h is height of tree (O(n) worst case)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert a value into BST"""
        if not self.root:
            self.root = TreeNode(val)
            return
        
        self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

def inorder_traversal_recursive(root):
    """Inorder traversal: Left -> Root -> Right"""
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

def inorder_traversal_iterative(root):
    """Iterative inorder traversal using stack"""
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Reach the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result

def preorder_traversal_recursive(root):
    """Preorder traversal: Root -> Left -> Right"""
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result

def preorder_traversal_iterative(root):
    """Iterative preorder traversal using stack"""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        current = stack.pop()
        result.append(current.val)
        
        # Push right child first (so left is processed first)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return result

def postorder_traversal_recursive(root):
    """Postorder traversal: Left -> Right -> Root"""
    result = []
    
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
    
    postorder(root)
    return result

def postorder_traversal_iterative(root):
    """Iterative postorder traversal using two stacks"""
    if not root:
        return []
    
    result = []
    stack1 = [root]
    stack2 = []
    
    while stack1:
        current = stack1.pop()
        stack2.append(current)
        
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)
    
    while stack2:
        result.append(stack2.pop().val)
    
    return result

def level_order_traversal(root):
    """Level order traversal (BFS) using queue"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            current = queue.pop(0)
            level.append(current.val)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        result.append(level)
    
    return result

def level_order_traversal_single_list(root):
    """Level order traversal returning single list"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        result.append(current.val)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result

def morris_inorder_traversal(root):
    """Morris inorder traversal - O(1) space complexity"""
    result = []
    current = root
    
    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right
    
    return result

def morris_preorder_traversal(root):
    """Morris preorder traversal - O(1) space complexity"""
    result = []
    current = root
    
    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                result.append(current.val)
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                current = current.right
    
    return result

def zigzag_level_order_traversal(root):
    """Zigzag level order traversal"""
    if not root:
        return []
    
    result = []
    queue = [root]
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            current = queue.pop(0)
            
            if left_to_right:
                level.append(current.val)
            else:
                level.insert(0, current.val)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        result.append(level)
        left_to_right = not left_to_right
    
    return result

def vertical_order_traversal(root):
    """Vertical order traversal"""
    if not root:
        return []
    
    # Dictionary to store nodes by column
    column_map = {}
    min_col = max_col = 0
    
    def dfs(node, row, col):
        nonlocal min_col, max_col
        
        if not node:
            return
        
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        
        if col not in column_map:
            column_map[col] = []
        column_map[col].append((row, node.val))
        
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)
    
    dfs(root, 0, 0)
    
    # Sort nodes in each column by row and value
    for col in column_map:
        column_map[col].sort()
    
    # Build result
    result = []
    for col in range(min_col, max_col + 1):
        if col in column_map:
            result.append([val for _, val in column_map[col]])
    
    return result

def boundary_traversal(root):
    """Boundary traversal of binary tree"""
    if not root:
        return []
    
    result = []
    
    # Add root
    result.append(root.val)
    
    # Add left boundary (excluding leaf)
    def add_left_boundary(node):
        if not node or (not node.left and not node.right):
            return
        result.append(node.val)
        if node.left:
            add_left_boundary(node.left)
        else:
            add_left_boundary(node.right)
    
    # Add leaves
    def add_leaves(node):
        if not node:
            return
        if not node.left and not node.right:
            result.append(node.val)
        else:
            add_leaves(node.left)
            add_leaves(node.right)
    
    # Add right boundary (excluding leaf, in reverse)
    def add_right_boundary(node):
        if not node or (not node.left and not node.right):
            return
        if node.right:
            add_right_boundary(node.right)
        else:
            add_right_boundary(node.left)
        result.append(node.val)
    
    add_left_boundary(root.left)
    add_leaves(root)
    add_right_boundary(root.right)
    
    return result

# Example usage and testing
if __name__ == "__main__":
    # Create a sample BST
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    
    for val in values:
        bst.insert(val)
    
    print("Binary Search Tree Traversal Algorithms")
    print("=" * 50)
    print(f"Tree values: {values}")
    print()
    
    # Test different traversal methods
    print("1. Inorder Traversal (Left -> Root -> Right):")
    print(f"   Recursive: {inorder_traversal_recursive(bst.root)}")
    print(f"   Iterative: {inorder_traversal_iterative(bst.root)}")
    print(f"   Morris: {morris_inorder_traversal(bst.root)}")
    print()
    
    print("2. Preorder Traversal (Root -> Left -> Right):")
    print(f"   Recursive: {preorder_traversal_recursive(bst.root)}")
    print(f"   Iterative: {preorder_traversal_iterative(bst.root)}")
    print(f"   Morris: {morris_preorder_traversal(bst.root)}")
    print()
    
    print("3. Postorder Traversal (Left -> Right -> Root):")
    print(f"   Recursive: {postorder_traversal_recursive(bst.root)}")
    print(f"   Iterative: {postorder_traversal_iterative(bst.root)}")
    print()
    
    print("4. Level Order Traversal (BFS):")
    print(f"   Level by level: {level_order_traversal(bst.root)}")
    print(f"   Single list: {level_order_traversal_single_list(bst.root)}")
    print()
    
    print("5. Zigzag Level Order Traversal:")
    print(f"   Result: {zigzag_level_order_traversal(bst.root)}")
    print()
    
    print("6. Vertical Order Traversal:")
    print(f"   Result: {vertical_order_traversal(bst.root)}")
    print()
    
    print("7. Boundary Traversal:")
    print(f"   Result: {boundary_traversal(bst.root)}")
    print()
    
    # Performance comparison
    print("=" * 50)
    print("Performance Comparison:")
    
    import time
    
    # Test with larger tree
    large_bst = BinarySearchTree()
    large_values = list(range(1, 1001))
    for val in large_values:
        large_bst.insert(val)
    
    # Test recursive vs iterative
    start = time.time()
    inorder_traversal_recursive(large_bst.root)
    recursive_time = time.time() - start
    
    start = time.time()
    inorder_traversal_iterative(large_bst.root)
    iterative_time = time.time() - start
    
    start = time.time()
    morris_inorder_traversal(large_bst.root)
    morris_time = time.time() - start
    
    print(f"Recursive inorder: {recursive_time:.6f}s")
    print(f"Iterative inorder: {iterative_time:.6f}s")
    print(f"Morris inorder: {morris_time:.6f}s") 