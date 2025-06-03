from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

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

def print_list(head: Optional[ListNode]) -> str:
    """Helper function to print linked list"""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return "->".join(values) if values else "None"

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Test case 1:")
    print(f"Original list: {print_list(head1)}")
    reversed_head1 = reverse_list(head1)
    print(f"Reversed list: {print_list(reversed_head1)}")
    
    # Test case 2: Two nodes
    head2 = ListNode(1, ListNode(2))
    print("\nTest case 2:")
    print(f"Original list: {print_list(head2)}")
    reversed_head2 = reverse_list(head2)
    print(f"Reversed list: {print_list(reversed_head2)}")
    
    # Test case 3: Single node
    head3 = ListNode(1)
    print("\nTest case 3:")
    print(f"Original list: {print_list(head3)}")
    reversed_head3 = reverse_list(head3)
    print(f"Reversed list: {print_list(reversed_head3)}")
    
    # Test case 4: Empty list
    head4 = None
    print("\nTest case 4:")
    print(f"Original list: {print_list(head4)}")
    reversed_head4 = reverse_list(head4)
    print(f"Reversed list: {print_list(reversed_head4)}")
    
    # Test case 5: Longer list
    head5 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print("\nTest case 5:")
    print(f"Original list: {print_list(head5)}")
    reversed_head5 = reverse_list(head5)
    print(f"Reversed list: {print_list(reversed_head5)}") 