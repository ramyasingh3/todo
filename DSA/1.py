from solution import reverseList, createLinkedList, ListNode

def test_reverse_linked_list():
    # Test case 1: Normal list
    arr1 = [1, 2, 3, 4, 5]
    head1 = createLinkedList(arr1)
    reversed_head1 = reverseList(head1)
    result1 = []
    curr = reversed_head1
    while curr:
        result1.append(curr.val)
        curr = curr.next
    assert result1 == [5, 4, 3, 2, 1], "Test case 1 failed"
    
    # Test case 2: Empty list
    head2 = None
    reversed_head2 = reverseList(head2)
    assert reversed_head2 is None, "Test case 2 failed"
    
    # Test case 3: Single node
    head3 = createLinkedList([1])
    reversed_head3 = reverseList(head3)
    result3 = []
    curr = reversed_head3
    while curr:
        result3.append(curr.val)
        curr = curr.next
    assert result3 == [1], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_reverse_linked_list()