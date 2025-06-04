"""
Palindrome Linked List Implementation

This file contains an implementation to check if a linked list is a palindrome.

Problem Statement:
Given the head of a singly linked list, determine if it is a palindrome.
A palindrome reads the same forwards and backwards.

Time Complexity: O(n)
Space Complexity: O(1) for the optimal solution
"""

class ListNode:
    """Node class for singly linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    """
    Check if a linked list is a palindrome using the two-pointer technique.
    
    Args:
        head (ListNode): Head of the linked list
        
    Returns:
        bool: True if the list is a palindrome, False otherwise
    """
    # Empty list or single node is a palindrome
    if not head or not head.next:
        return True
    
    # Find the middle of the list using slow and fast pointers
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the list
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # Compare the first half with the reversed second half
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True

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

def test_palindrome_linked_list():
    """Test cases for palindrome linked list"""
    # Test case 1: Empty list
    assert is_palindrome(None) == True, "Test case 1 failed"
    
    # Test case 2: Single node
    head1 = ListNode(1)
    assert is_palindrome(head1) == True, "Test case 2 failed"
    
    # Test case 3: Palindrome with even length
    list1 = create_linked_list([1, 2, 2, 1])
    assert is_palindrome(list1) == True, "Test case 3 failed"
    
    # Test case 4: Palindrome with odd length
    list2 = create_linked_list([1, 2, 3, 2, 1])
    assert is_palindrome(list2) == True, "Test case 4 failed"
    
    # Test case 5: Not a palindrome
    list3 = create_linked_list([1, 2, 3, 4])
    assert is_palindrome(list3) == False, "Test case 5 failed"
    
    # Test case 6: Palindrome with repeated numbers
    list4 = create_linked_list([1, 1, 1, 1])
    assert is_palindrome(list4) == True, "Test case 6 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_palindrome_linked_list()
    
    # Example usage
    test_cases = [
        [1, 2, 2, 1],      # Even length palindrome
        [1, 2, 3, 2, 1],   # Odd length palindrome
        [1, 2, 3, 4],      # Not a palindrome
        [1, 1, 1, 1],      # All same numbers
        [1],               # Single node
        []                 # Empty list
    ]
    
    print("\nTesting various linked lists:")
    for values in test_cases:
        head = create_linked_list(values)
        result = is_palindrome(head)
        print(f"List: {values} -> Is Palindrome: {result}") 