from typing import Any, Optional
from dataclasses import dataclass

@dataclass
class StackNode:
    """Node class for Stack"""
    value: Any
    next: Optional['StackNode'] = None

class Stack:
    """Stack implementation using linked list"""
    
    def __init__(self):
        """Initialize empty stack"""
        self.top: Optional[StackNode] = None
        self.size = 0
    
    def push(self, value: Any) -> None:
        """
        Push value onto stack
        
        Args:
            value: Value to push
        """
        new_node = StackNode(value, self.top)
        self.top = new_node
        self.size += 1
    
    def pop(self) -> Any:
        """
        Pop value from stack
        
        Returns:
            Value from top of stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value
    
    def peek(self) -> Any:
        """
        Get top value without removing it
        
        Returns:
            Value from top of stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value
    
    def is_empty(self) -> bool:
        """Check if stack is empty"""
        return self.size == 0
    
    def get_size(self) -> int:
        """Get number of elements in stack"""
        return self.size

# Example usage
if __name__ == "__main__":
    # Create a stack
    stack = Stack()
    
    # Test push
    print("Testing push:")
    values = [1, 2, 3, 4, 5]
    for value in values:
        stack.push(value)
        print(f"Pushed: {value}")
        print(f"Top element: {stack.peek()}")
        print(f"Stack size: {stack.get_size()}")
    
    # Test pop
    print("\nTesting pop:")
    while not stack.is_empty():
        value = stack.pop()
        print(f"Popped: {value}")
        if not stack.is_empty():
            print(f"New top element: {stack.peek()}")
        print(f"Stack size: {stack.get_size()}")
    
    # Test empty stack
    print("\nTesting empty stack:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error: {e}")
    
    try:
        stack.peek()
    except IndexError as e:
        print(f"Error: {e}") 