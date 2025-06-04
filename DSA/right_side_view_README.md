# Binary Tree Right Side View

## Problem Description
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Examples

### Example 1
```
Input:
    1
   / \
  2   3
   \   \
    5   4

Output: [1, 3, 4]
```

### Example 2
```
Input:
    1
   /
  2
 /
3

Output: [1, 2, 3]
```

### Example 3
```
Input:
    1
     \
      2
       \
        3

Output: [1, 2, 3]
```

## Solution Approach
The solution uses a breadth-first search (BFS) approach with a queue to traverse the tree level by level. For each level, we only keep the rightmost node's value.

### Algorithm Steps:
1. Initialize an empty result list and a queue with the root node
2. While the queue is not empty:
   - Get the current level size
   - Process all nodes in the current level
   - For each node, add its children to the queue
   - Only add the last node's value of each level to the result
3. Return the result list

## Time Complexity
- O(N) where N is the number of nodes in the tree
- Each node is visited exactly once

## Space Complexity
- O(W) where W is the maximum width of the tree
- In the worst case, the queue can hold up to N/2 nodes (for a complete binary tree)

## Implementation Details

### TreeNode Class
- `val`: Node value
- `left`: Left child
- `right`: Right child

### Solution Class
- `rightSideView`: Main method that returns the right side view of the tree
- Uses BFS with a queue to traverse the tree level by level
- Only keeps the rightmost node of each level

### Helper Functions
- `build_tree`: Constructs a binary tree from a list of values
- `print_tree`: Prints the tree in a readable format

## Test Cases
1. Simple tree with right side view [1, 3, 4]
2. Tree with only left children [1, 2, 3, 4]
3. Empty tree []
4. Tree with only right children [1, 2, 3]
5. Complex complete binary tree [1, 3, 7, 15]

## Running the Tests
```bash
python right_side_view.py
```

## Common Applications
- Tree visualization
- Level order traversal variations
- Tree structure analysis
- Binary tree problem solving 