from collections import deque

class Queue:
    def __init__(self):
        # Initialize an empty deque to hold queue elements
        self.items = deque()
    
    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0
    
    def enqueue(self, data):
        # Add an item to the rear of the queue
        self.items.append(data)
    
    def dequeue(self):
        # Remove and return the item from the front of the queue
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Queue is empty")
    
    def get_front(self):
        # Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")
    
    def get_rear(self):
        # Return the item at the rear of the queue without removing it
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")
    
    def size(self):
        # Return the number of items in the queue
        return len(self.items)
    
    def display(self):
        # Print the current queue elements
        print(list(self.items))

# Example usage
Q1 = Queue()
Q1.enqueue(10)
Q1.enqueue(20)
Q1.enqueue(30)
print(Q1.get_front())  # Output: 10
print(Q1.get_rear())   # Output: 30
print(Q1.dequeue())    # Output: 10
Q1.display()          # Output: [20, 30]
