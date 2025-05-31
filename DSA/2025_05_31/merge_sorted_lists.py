class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists and return it as a new sorted list.
    
    Args:
        l1: First sorted linked list
        l2: Second sorted linked list
        
    Returns:
        Merged sorted linked list
        
    Example:
        >>> l1 = ListNode(1, ListNode(2, ListNode(4)))
        >>> l2 = ListNode(1, ListNode(3, ListNode(4)))
        >>> result = merge_two_lists(l1, l2)
        >>> # result should be 1->1->2->3->4->4
    """
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    result = merge_two_lists(l1, l2)
    print("Test case 1:")
    print("Merged list:", end=" ")
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
    
    # Test case 2: Empty lists
    l3 = None
    l4 = None
    result = merge_two_lists(l3, l4)
    print("\nTest case 2:")
    print("Merged list:", end=" ")
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
    
    # Test case 3: One empty list
    l5 = ListNode(1, ListNode(2, ListNode(3)))
    l6 = None
    result = merge_two_lists(l5, l6)
    print("\nTest case 3:")
    print("Merged list:", end=" ")
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
    
    # Test case 4: Lists with same values
    l7 = ListNode(1, ListNode(1, ListNode(1)))
    l8 = ListNode(1, ListNode(1, ListNode(1)))
    result = merge_two_lists(l7, l8)
    print("\nTest case 4:")
    print("Merged list:", end=" ")
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
    
    # Test case 5: Lists with different lengths
    l9 = ListNode(1, ListNode(2))
    l10 = ListNode(3, ListNode(4, ListNode(5)))
    result = merge_two_lists(l9, l10)
    print("\nTest case 5:")
    print("Merged list:", end=" ")
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None") 