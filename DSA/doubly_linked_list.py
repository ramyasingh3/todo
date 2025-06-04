from typing import Optional, Any

class Node:
    """Node class for Doubly Linked List"""
    def __init__(self, data: Any):
        self.data = data
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

class DoublyLinkedList:
    """Doubly Linked List implementation"""
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0
    
    def insert_at_beginning(self, data: Any) -> None:
        """
        Insert a node at the beginning of the list
        
        Args:
            data: Data to be inserted
        """
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data: Any) -> None:
        """
        Insert a node at the end of the list
        
        Args:
            data: Data to be inserted
        """
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def insert_at_position(self, data: Any, position: int) -> bool:
        """
        Insert a node at the specified position
        
        Args:
            data: Data to be inserted
            position: Position to insert at (0-based)
            
        Returns:
            True if insertion was successful, False otherwise
        """
        if position < 0 or position > self.size:
            return False
            
        if position == 0:
            self.insert_at_beginning(data)
            return True
            
        if position == self.size:
            self.insert_at_end(data)
            return True
            
        new_node = Node(data)
        current = self.head
        for _ in range(position):
            current = current.next
            
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self.size += 1
        return True
    
    def delete_at_beginning(self) -> Optional[Any]:
        """
        Delete the first node in the list
        
        Returns:
            Data of the deleted node, None if list is empty
        """
        if not self.head:
            return None
            
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data
    
    def delete_at_end(self) -> Optional[Any]:
        """
        Delete the last node in the list
        
        Returns:
            Data of the deleted node, None if list is empty
        """
        if not self.tail:
            return None
            
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data
    
    def delete_at_position(self, position: int) -> Optional[Any]:
        """
        Delete a node at the specified position
        
        Args:
            position: Position to delete from (0-based)
            
        Returns:
            Data of the deleted node, None if position is invalid
        """
        if position < 0 or position >= self.size:
            return None
            
        if position == 0:
            return self.delete_at_beginning()
            
        if position == self.size - 1:
            return self.delete_at_end()
            
        current = self.head
        for _ in range(position):
            current = current.next
            
        data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return data
    
    def get_at_position(self, position: int) -> Optional[Any]:
        """
        Get data at the specified position
        
        Args:
            position: Position to get data from (0-based)
            
        Returns:
            Data at the position, None if position is invalid
        """
        if position < 0 or position >= self.size:
            return None
            
        current = self.head
        for _ in range(position):
            current = current.next
            
        return current.data
    
    def display_forward(self) -> None:
        """Display the list from head to tail"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    def display_backward(self) -> None:
        """Display the list from tail to head"""
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Example usage
if __name__ == "__main__":
    # Create a doubly linked list
    dll = DoublyLinkedList()
    
    # Test insertion
    print("Testing insertion:")
    dll.insert_at_beginning(1)
    dll.insert_at_end(2)
    dll.insert_at_position(3, 1)
    dll.insert_at_beginning(0)
    dll.insert_at_end(4)
    
    print("\nForward traversal:")
    dll.display_forward()
    print("Backward traversal:")
    dll.display_backward()
    
    # Test deletion
    print("\nTesting deletion:")
    print(f"Deleted from beginning: {dll.delete_at_beginning()}")
    print(f"Deleted from end: {dll.delete_at_end()}")
    print(f"Deleted at position 1: {dll.delete_at_position(1)}")
    
    print("\nList after deletions:")
    dll.display_forward()
    
    # Test get operation
    print("\nTesting get operation:")
    for i in range(dll.size):
        print(f"Data at position {i}: {dll.get_at_position(i)}")
    
    # Test edge cases
    print("\nTesting edge cases:")
    print(f"Get at invalid position: {dll.get_at_position(10)}")
    print(f"Delete at invalid position: {dll.delete_at_position(10)}")
    print(f"Insert at invalid position: {dll.insert_at_position(5, 10)}") 