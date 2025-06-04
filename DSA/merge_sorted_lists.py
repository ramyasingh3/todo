"""
Merge Two Sorted Lists Implementation

This file contains an implementation of merging two sorted linked lists into a single sorted list.

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Time Complexity: O(n + m) where n and m are the lengths of the input lists
Space Complexity: O(1) as we only use a constant amount of extra space
"""

class ListNode:
    """Node class for singly linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted linked lists into one sorted list.
    
    Args:
        list1 (ListNode): Head of first sorted linked list
        list2 (ListNode): Head of second sorted linked list
        
    Returns:
        ListNode: Head of the merged sorted linked list
    """
    # Create a dummy node to handle edge cases
    dummy = ListNode(0)
    current = dummy
    
    # Compare and merge nodes from both lists
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining nodes from either list
    current.next = list1 if list1 else list2
    
    return dummy.next

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

def test_merge_sorted_lists():
    """Test cases for merging sorted linked lists"""
    # Test case 1: Both lists have elements
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])
    result = merge_sorted_lists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6], "Test case 1 failed"
    
    # Test case 2: One list is empty
    list1 = create_linked_list([1, 2, 3])
    list2 = None
    result = merge_sorted_lists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3], "Test case 2 failed"
    
    # Test case 3: Both lists are empty
    result = merge_sorted_lists(None, None)
    assert linked_list_to_list(result) == [], "Test case 3 failed"
    
    # Test case 4: Lists with different lengths
    list1 = create_linked_list([1, 3, 5, 7])
    list2 = create_linked_list([2, 4])
    result = merge_sorted_lists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 7], "Test case 4 failed"
    
    # Test case 5: Lists with duplicate values
    list1 = create_linked_list([1, 1, 2, 3])
    list2 = create_linked_list([1, 2, 2, 4])
    result = merge_sorted_lists(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 1, 2, 2, 2, 3, 4], "Test case 5 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_merge_sorted_lists()
    
    # Example usage
    # Create two sorted linked lists
    list1 = create_linked_list([1, 3, 5, 7])
    list2 = create_linked_list([2, 4, 6, 8])
    
    print("First sorted list:", linked_list_to_list(list1))
    print("Second sorted list:", linked_list_to_list(list2))
    
    # Merge the lists
    merged_list = merge_sorted_lists(list1, list2)
    print("Merged sorted list:", linked_list_to_list(merged_list)) 