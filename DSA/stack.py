from typing import Any, Optional

class Stack:
    """Stack implementation using a list"""
    
    def __init__(self):
        self.items: list[Any] = []
    
    def push(self, item: Any) -> None:
        """
        Push an item onto the stack
        
        Args:
            item: Item to be pushed
        """
        self.items.append(item)
    
    def pop(self) -> Optional[Any]:
        """
        Pop an item from the stack
        
        Returns:
            The popped item, None if stack is empty
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self) -> Optional[Any]:
        """
        Get the top item without removing it
        
        Returns:
            The top item, None if stack is empty
        """
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty
        
        Returns:
            True if stack is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in the stack
        
        Returns:
            Number of items in the stack
        """
        return len(self.items)

# Example usage
if __name__ == "__main__":
    # Create a stack
    stack = Stack()
    
    # Test push
    print("Testing push:")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack size: {stack.size()}")
    print(f"Top element: {stack.peek()}")
    
    # Test pop
    print("\nTesting pop:")
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack size: {stack.size()}")
    print(f"Top element: {stack.peek()}")
    
    # Test empty stack
    print("\nTesting empty stack:")
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")  # Should return None
    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Top element: {stack.peek()}")  # Should return None 