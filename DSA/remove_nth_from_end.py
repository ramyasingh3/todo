class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Create a dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize two pointers
    first = dummy
    second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node from the end
    second.next = second.next.next
    
    return dummy.next

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def printLinkedList(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)

# Test the solution
if __name__ == "__main__":
    # Test case 1: [1,2,3,4,5], n=2
    test_values1 = [1, 2, 3, 4, 5]
    head1 = createLinkedList(test_values1)
    n1 = 2
    
    print("Test Case 1:")
    print("Original linked list:")
    print(printLinkedList(head1))
    
    result1 = removeNthFromEnd(head1, n1)
    print(f"\nAfter removing {n1}th node from end:")
    print(printLinkedList(result1))
    
    # Test case 2: [1], n=1
    test_values2 = [1]
    head2 = createLinkedList(test_values2)
    n2 = 1
    
    print("\nTest Case 2:")
    print("Original linked list:")
    print(printLinkedList(head2))
    
    result2 = removeNthFromEnd(head2, n2)
    print(f"\nAfter removing {n2}th node from end:")
    print(printLinkedList(result2)) 