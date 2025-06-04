# Data Structures and Algorithms

This repository contains implementations of various data structures and algorithms problems.

## Problems Implemented

1. **Binary Search Tree (BST)**
   - Basic BST operations
   - Search, Insert, Delete
   - Tree traversals

2. **AVL Tree**
   - Self-balancing BST implementation
   - Automatic balancing after insertions
   - Supports all BST operations in O(log n) time
   - Includes visualization tools

3. **String Problems**
   - Valid Parentheses
   - Longest Palindromic Substring
   - Minimum Window Substring
   - Longest Substring Without Repeating Characters
   - Find All Anagrams in a String

4. **Array Problems**
   - 3Sum
   - Container With Most Water
   - Trapping Rain Water

## AVL Tree Implementation

### Features
1. Self-balancing binary search tree
2. Maintains O(log n) height
3. Supports efficient insertions with automatic rebalancing
4. Includes visualization tools for tree structure

### Operations
- Insert a value
- Inorder traversal
- Print tree structure with heights
- Automatic balancing (Left/Right rotations)

### Example Usage
```python
# Create an AVL tree
avl_tree = AVLTree()

# Insert values
avl_tree.insert_value(10)
avl_tree.insert_value(20)
avl_tree.insert_value(30)

# Print tree structure
avl_tree.print_tree(avl_tree.root)

# Get inorder traversal
result = avl_tree.inorder_traversal(avl_tree.root)
```

### Time Complexity
- All operations: O(log n)
- Tree remains balanced after each operation

## Running the Code

### Prerequisites
- Python 3.x

### Running Tests
```bash
# Run AVL Tree tests
python avl_tree.py

# Run other implementations
python [filename].py
```

## Directory Structure
```
.
├── README.md
├── avl_tree.py         # AVL Tree implementation
├── valid_parentheses.py
├── three_sum.py
├── longest_palindromic_substring.py
├── minimum_window_substring.py
├── trapping_rain_water.py
├── container_with_most_water.py
├── longest_substring_without_repeating.py
├── find_all_anagrams.py
└── [other files]       # Other implementations
```

## Contributing
Feel free to contribute by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License
This project is open source and available under the MIT License.

## Problems Solved

### 1. Reverse Linked List (LeetCode #206)
Given the head of a singly linked list, reverse the list, and return the reversed list.

#### Solution Approach
The solution uses an iterative approach to reverse the linked list:
1. Initialize a `prev` pointer as `None` (this will be the new head of the reversed list)
2. Keep track of the current node
3. For each node:
   - Store the next node temporarily
   - Reverse the link by pointing current node to previous node
   - Move the previous and current pointers forward
4. Return the new head (which will be the last node of the original list)

#### Time Complexity
- O(n) where n is the number of nodes in the linked list

#### Space Complexity
- O(1) as we only use a constant amount of extra space

#### Example
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1

### 2. Remove Nth Node From End of List (LeetCode #19)
Given the head of a linked list, remove the nth node from the end of the list and return its head.

#### Solution Approach
The solution uses the two-pointer technique:
1. Create a dummy node to handle edge cases
2. Initialize two pointers (first and second) at the dummy node
3. Move the first pointer n+1 steps ahead
4. Move both pointers until the first pointer reaches the end
5. Remove the nth node by updating the second pointer's next reference

#### Time Complexity
- O(n) where n is the number of nodes in the linked list

#### Space Complexity
- O(1) as we only use a constant amount of extra space

#### Example
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

## Progress Tracker

### Completed Problems
- [x] Reverse Linked List (LeetCode #206)
- [x] Remove Nth Node From End of List (LeetCode #19)

### In Progress
- [ ] Merge Two Sorted Lists (LeetCode #21)
- [ ] Linked List Cycle (LeetCode #141)

### Next Up
- [ ] Add Two Numbers (LeetCode #2)
- [ ] Remove Duplicates from Sorted List (LeetCode #83)

---
*Note: This repository is part of my daily coding practice and DSA learning journey. Last updated: 2024-03-19*
