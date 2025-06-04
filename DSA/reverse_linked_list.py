"""
Reverse Linked List Implementation

This file contains an implementation of a singly linked list and the algorithm to reverse it.

Problem Statement:
Given the head of a singly linked list, reverse the list and return the reversed list.

Time Complexity: O(n)
Space Complexity: O(1) for iterative approach, O(n) for recursive approach
"""

class ListNode:
    """Node class for singly linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list_iterative(head):
    """
    Reverse a linked list using iterative approach.
    
    Args:
        head (ListNode): Head of the linked list
        
    Returns:
        ListNode: Head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        # Store next node
        next_node = current.next
        # Reverse current node's pointer
        current.next = prev
        # Move prev and current one step forward
        prev = current
        current = next_node
    
    return prev

def reverse_linked_list_recursive(head):
    """
    Reverse a linked list using recursive approach.
    
    Args:
        head (ListNode): Head of the linked list
        
    Returns:
        ListNode: Head of the reversed linked list
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursive case: reverse the rest of the list
    new_head = reverse_linked_list_recursive(head.next)
    
    # Reverse the link between current node and next node
    head.next.next = head
    head.next = None
    
    return new_head

def create_linked_list(values):
    """
    Create a linked list from a list of values.
    
    Args:
        values (list): List of values to create nodes from
        
    Returns:
        ListNode: Head of the created linked list
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """
    Convert a linked list to a Python list.
    
    Args:
        head (ListNode): Head of the linked list
        
    Returns:
        list: List of values from the linked list
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_reverse_linked_list():
    """Test cases for linked list reversal"""
    # Test case 1: Empty list
    assert linked_list_to_list(reverse_linked_list_iterative(None)) == [], "Iterative test case 1 failed"
    assert linked_list_to_list(reverse_linked_list_recursive(None)) == [], "Recursive test case 1 failed"
    
    # Test case 2: Single node
    head1 = ListNode(1)
    assert linked_list_to_list(reverse_linked_list_iterative(head1)) == [1], "Iterative test case 2 failed"
    assert linked_list_to_list(reverse_linked_list_recursive(head1)) == [1], "Recursive test case 2 failed"
    
    # Test case 3: Multiple nodes
    head2 = create_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(reverse_linked_list_iterative(head2)) == [5, 4, 3, 2, 1], "Iterative test case 3 failed"
    
    head3 = create_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(reverse_linked_list_recursive(head3)) == [5, 4, 3, 2, 1], "Recursive test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_reverse_linked_list()
    
    # Example usage
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original linked list:", linked_list_to_list(head))
    
    # Reverse using iterative approach
    reversed_head_iterative = reverse_linked_list_iterative(head)
    print("Reversed (iterative):", linked_list_to_list(reversed_head_iterative))
    
    # Create another linked list for recursive approach
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head_recursive = reverse_linked_list_recursive(head)
    print("Reversed (recursive):", linked_list_to_list(reversed_head_recursive)) 