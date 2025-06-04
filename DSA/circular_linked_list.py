from typing import Optional, Any

class Node:
    """Node class for Circular Linked List"""
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[Node] = None

class CircularLinkedList:
    """Circular Linked List implementation"""
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.size: int = 0
    
    def insert_at_beginning(self, data: Any) -> None:
        """
        Insert a node at the beginning of the list
        
        Args:
            data: Data to be inserted
        """
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data: Any) -> None:
        """
        Insert a node at the end of the list
        
        Args:
            data: Data to be inserted
        """
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
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
        for _ in range(position - 1):
            current = current.next
            
        new_node.next = current.next
        current.next = new_node
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
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        self.size -= 1
        return data
    
    def delete_at_end(self) -> Optional[Any]:
        """
        Delete the last node in the list
        
        Returns:
            Data of the deleted node, None if list is empty
        """
        if not self.head:
            return None
            
        if self.head.next == self.head:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
            
        current = self.head
        while current.next.next != self.head:
            current = current.next
            
        data = current.next.data
        current.next = self.head
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
        for _ in range(position - 1):
            current = current.next
            
        data = current.next.data
        current.next = current.next.next
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
    
    def display(self) -> None:
        """Display the list"""
        if not self.head:
            print("Empty list")
            return
            
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Example usage
if __name__ == "__main__":
    # Create a circular linked list
    cll = CircularLinkedList()
    
    # Test insertion
    print("Testing insertion:")
    cll.insert_at_beginning(1)
    cll.insert_at_end(2)
    cll.insert_at_position(3, 1)
    cll.insert_at_beginning(0)
    cll.insert_at_end(4)
    
    print("\nList after insertions:")
    cll.display()
    
    # Test deletion
    print("\nTesting deletion:")
    print(f"Deleted from beginning: {cll.delete_at_beginning()}")
    print(f"Deleted from end: {cll.delete_at_end()}")
    print(f"Deleted at position 1: {cll.delete_at_position(1)}")
    
    print("\nList after deletions:")
    cll.display()
    
    # Test get operation
    print("\nTesting get operation:")
    for i in range(cll.size):
        print(f"Data at position {i}: {cll.get_at_position(i)}")
    
    # Test edge cases
    print("\nTesting edge cases:")
    print(f"Get at invalid position: {cll.get_at_position(10)}")
    print(f"Delete at invalid position: {cll.delete_at_position(10)}")
    print(f"Insert at invalid position: {cll.insert_at_position(5, 10)}") 