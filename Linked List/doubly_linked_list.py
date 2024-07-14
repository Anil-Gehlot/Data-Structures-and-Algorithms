
class Node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next
    

class DLL:
    def __init__(self, head=None) :
        self.head = head
    def is_empty(self):
        return self.head == None

    def insert_at_start(self, data):
        node = Node(None, data, self.head)
        self.head = node 
    
    def insert_at_last(self, data):

        temp = self.head
        if temp is not None:
            while temp.next:
                temp = temp.next
        
        node = Node(temp, data, None)
        if temp is not None:
            temp.next = node
        else:
            self.head = node
    
    def serach(self, data):
        temp = self.head
        while temp:
            if temp.data == data :
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, data, node_data):
        temp = self.serach(node_data)

        if temp is None:
            print(f"Node with data {node_data} not found.")
            return

        node = Node(temp, data, temp.next)
        if temp.next:
            temp.next.prev = node
        temp.next = node
    
    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            
    def delete_first(self):
        if self.head:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
        else:
            print("List is empty.")
    
    def delete_last(self):
        if self.head:
            # Traverse to the last node
            temp = self.head
            while temp.next:
                temp = temp.next
            
            # Now temp points to the last node
            if temp.prev:
                temp.prev.next = None  # Remove the link from the previous node
            else:
                self.head = None  # If temp.prev is None, it means temp is the only node
        
        else:
            print("List is empty.")
