class PriorityQueue:
    def __init__(self):
        # Initialize an empty list to hold queue elements
        self.items = []
    
    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0
    
    def push(self, data, priority):
        # Insert element in the correct position based on its priority
        index = 0
        while index < len(self.items) and priority >= self.items[index][1]:
            index += 1
        self.items.insert(index, (data, priority))
    
    def pop(self):
        # Remove and return the element with the highest priority
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.items.pop(0)[0]


    def size(self):
        # Return the number of elements in the queue
        return len(self.items)

    def display(self):
        # Print the current queue elements
        print(self.items)

# Example usage
pq = PriorityQueue()
pq.push("task1", 4)
pq.push("task2", 3)
pq.push("task3", 2)
print(pq.pop())     # Output: task3
pq.display()        # Output: [('task2', 3), ('task1', 4)]
