# Binary Tree Maximum Path Sum

## Problem Description
Given a binary tree, find the maximum path sum. A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

## Examples

### Example 1: Simple Tree
```
    1
   / \
  2   3
```
Maximum path sum: 6 (path: 2 -> 1 -> 3)

### Example 2: Tree with Negative Values
```
    -10
    /  \
   9   20
      /  \
     15   7
```
Maximum path sum: 42 (path: 15 -> 20 -> 7)

### Example 3: Single Node Tree
```
    -3
```
Maximum path sum: -3 (single node path)

## Solution Approach
The solution uses a recursive approach with the following key points:

1. **Recursive Function**: `max_gain(node)`
   - Returns the maximum gain one can get by continuing the same path
   - Considers both left and right subtrees
   - Updates the global maximum sum when a better path is found

2. **Key Steps**:
   - Calculate maximum gains from left and right subtrees
   - Consider only positive gains (using max(0, gain))
   - Calculate the price of a new path where current node is the highest
   - Update global maximum if a better path is found
   - Return the maximum gain for continuing the same path

3. **Time Complexity**: O(N), where N is the number of nodes in the tree
   - Each node is visited exactly once

4. **Space Complexity**: O(H), where H is the height of the tree
   - In worst case (skewed tree): O(N)
   - In balanced tree: O(log N)

## Usage
```python
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create Solution instance
solution = Solution()

# Find maximum path sum
max_sum = solution.maxPathSum(root)
print(f"Maximum path sum: {max_sum}")  # Output: 6
```

## Test Cases
The implementation includes three test cases:

1. **Simple Tree**:
   - Tree with positive values
   - Expected maximum path sum: 6

2. **Tree with Negative Values**:
   - Tree with both positive and negative values
   - Expected maximum path sum: 42

3. **Single Node Tree**:
   - Tree with only one node
   - Expected maximum path sum: -3

## Running the Tests
```bash
python max_path_sum.py
```

## Implementation Details
The implementation includes:
1. `TreeNode` class for creating binary tree nodes
2. `Solution` class with `maxPathSum` method
3. Helper functions:
   - `print_tree`: Visualizes the tree structure
   - `build_test_tree*`: Creates test trees
4. Comprehensive test cases with visual output

## Common Applications
- Network routing optimization
- Game tree evaluation
- Decision tree analysis
- Path finding in graphs 