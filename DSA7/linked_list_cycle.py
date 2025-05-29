class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
            
    return False

# Example usage
if __name__ == "__main__":
    # Create a linked list with a cycle
    head1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    head1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle
    
    # Create a linked list without a cycle
    head2 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    head2.next = node2
    node2.next = node3
    node3.next = node4
    
    # Test cases
    print("Linked List with cycle:", has_cycle(head1))  # Should print True
    print("Linked List without cycle:", has_cycle(head2))  # Should print False 