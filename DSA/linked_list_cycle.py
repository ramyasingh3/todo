"""
Linked List Cycle Detection Implementation

This file contains an implementation to detect if a linked list has a cycle using
Floyd's Cycle-Finding Algorithm (also known as the "tortoise and hare" algorithm).

Problem Statement:
Given the head of a linked list, determine if the linked list has a cycle in it.
A cycle exists if there is some node in the list that can be reached again by
continuously following the next pointer.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    """Node class for singly linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    """
    Detect if a linked list has a cycle using Floyd's Cycle-Finding Algorithm.
    
    Args:
        head (ListNode): Head of the linked list
        
    Returns:
        bool: True if the list has a cycle, False otherwise
    """
    # Empty list or single node cannot have a cycle
    if not head or not head.next:
        return False
    
    # Initialize slow and fast pointers
    slow = head
    fast = head
    
    # Move slow pointer by 1 and fast pointer by 2
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # If they meet, there is a cycle
        if slow == fast:
            return True
    
    # If fast pointer reaches end, there is no cycle
    return False

def create_linked_list(values, cycle_pos=-1):
    """
    Create a linked list from a list of values, optionally with a cycle.
    
    Args:
        values (list): List of values to create nodes from
        cycle_pos (int): Position to create cycle (-1 for no cycle)
        
    Returns:
        ListNode: Head of the created linked list
    """
    if not values:
        return None
    
    # Create nodes
    nodes = []
    for val in values:
        nodes.append(ListNode(val))
    
    # Connect nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if specified
    if cycle_pos >= 0 and cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]
    
    return nodes[0]

def linked_list_to_list(head, max_nodes=100):
    """
    Convert a linked list to a Python list, handling cycles.
    
    Args:
        head (ListNode): Head of the linked list
        max_nodes (int): Maximum number of nodes to process (to prevent infinite loops)
        
    Returns:
        list: List of values from the linked list
    """
    result = []
    current = head
    count = 0
    
    while current and count < max_nodes:
        result.append(current.val)
        current = current.next
        count += 1
    
    return result

def test_linked_list_cycle():
    """Test cases for linked list cycle detection"""
    # Test case 1: Empty list
    assert has_cycle(None) == False, "Test case 1 failed"
    
    # Test case 2: Single node
    head1 = ListNode(1)
    assert has_cycle(head1) == False, "Test case 2 failed"
    
    # Test case 3: List with cycle
    list1 = create_linked_list([1, 2, 3, 4], cycle_pos=1)
    assert has_cycle(list1) == True, "Test case 3 failed"
    
    # Test case 4: List without cycle
    list2 = create_linked_list([1, 2, 3, 4])
    assert has_cycle(list2) == False, "Test case 4 failed"
    
    # Test case 5: Self-loop
    head2 = ListNode(1)
    head2.next = head2
    assert has_cycle(head2) == True, "Test case 5 failed"
    
    # Test case 6: Two-node cycle
    list3 = create_linked_list([1, 2], cycle_pos=0)
    assert has_cycle(list3) == True, "Test case 6 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_linked_list_cycle()
    
    # Example usage
    test_cases = [
        ([1, 2, 3, 4], -1),    # No cycle
        ([1, 2, 3, 4], 1),     # Cycle at position 1
        ([1, 2, 3, 4], 0),     # Cycle at start
        ([1, 2, 3, 4], 3),     # Cycle at end
        ([1], -1),             # Single node
        ([], -1)               # Empty list
    ]
    
    print("\nTesting various linked lists:")
    for values, cycle_pos in test_cases:
        head = create_linked_list(values, cycle_pos)
        result = has_cycle(head)
        print(f"List: {values}, Cycle at position {cycle_pos} -> Has Cycle: {result}")

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