from collections import deque

class Stack:
    def __init__(self):
        # Initialize an empty deque to hold stack elements
        self.items = deque()
    
    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0
    
    def push(self, data):
        # Add an item to the top of the stack
        self.items.append(data)
    
    def pop(self):
        # Remove and return the item from the top of the stack
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        # Return the item at the top of the stack without removing it
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
            
    def size(self):
        # Return the number of items in the stack
        return len(self.items)
        
    def display(self):
        # Print the current stack elements
        print(list(self.items))

# Example usage
S1 = Stack()
S1.push(10)
S1.push(20)
S1.push(30)
print(S1.peek())  # Output: 30
print(S1.pop())   # Output: 30
S1.display()     # Output: [10, 20]
