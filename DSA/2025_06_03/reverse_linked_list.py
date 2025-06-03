from typing import Optional
from dataclasses import dataclass

@dataclass
class ListNode:
    """Node class for Linked List"""
    val: int
    next: Optional['ListNode'] = None

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list.
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
        
    Example:
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> reversed_head = reverse_list(head)
        >>> # reversed_head will be 3->2->1->None
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

def print_list(head: Optional[ListNode]) -> None:
    """Print the linked list"""
    current = head
    values = []
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values) + " -> None")

# Example usage
if __name__ == "__main__":
    # Test case 1: 1->2->3->4->5
    print("Test case 1:")
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original list:")
    print_list(head1)
    
    reversed_head1 = reverse_list(head1)
    print("Reversed list:")
    print_list(reversed_head1)
    
    # Test case 2: 1->2
    print("\nTest case 2:")
    head2 = ListNode(1, ListNode(2))
    print("Original list:")
    print_list(head2)
    
    reversed_head2 = reverse_list(head2)
    print("Reversed list:")
    print_list(reversed_head2)
    
    # Test case 3: Empty list
    print("\nTest case 3:")
    head3 = None
    print("Original list: None")
    
    reversed_head3 = reverse_list(head3)
    print("Reversed list:")
    print_list(reversed_head3) 