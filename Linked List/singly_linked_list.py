class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self, head=None):
        self.head = head
    
    def is_empty(self):
        return self.head == None
    
    def insert_at_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def insert_at_last(self, data):
        node = Node(data)

        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next 
            temp.next = node
        else:
            self.head = node

    def search(self, data):
        if not self.is_empty():
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    return temp
                temp = temp.next
        
        return None

    def insert_after(self, data, node_data):
        if self.is_empty():
            print("List is empty.")
            return
        
        temp = self.head
        node = Node(data)

        while temp is not None:
            if temp.data == node_data:
                node.next = temp.next
                temp.next = node
                break
            temp = temp.next

    
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next

    def delete_first(self):
        if not self.is_empty():
            self.head = self.head.next

    def delete_last(self):
        # Check if the list is empty
        if self.is_empty():
            print("List is empty.")
            return
        
        # Check if the list has only one node
        if self.head.next is None:
            self.head = None
            return
        
        # Traverse the list to find the second-to-last node
        temp = self.head
        while temp.next.next:
            temp = temp.next
        
        # Set the next of the second-to-last node to None
        temp.next = None
    
    def delete_node(self, value):
        if self.is_empty():
            print("List is empty.")
            return
        
        # If the node to be deleted is the head
        if self.head.data == value:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next


my_list = SLL()
my_list.insert_at_start(20)
my_list.insert_at_start(10)
my_list.insert_at_last(30)
my_list.insert_after(25, 20)

my_list.delete_node(30)
my_list.print_list()
print()