class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
    

from collections import deque
class BST:
    def __init__(self, data=None):
        self.root = Node(data)

    def rinsert(self, root, data):

        if root is None:
            return Node(data)

        if data < root.item:
            root.left = self.rinsert(root.left, data)
        
        elif data >= root.item:
            root.right = self.rinsert(root.right, data)
        return root
    
    def insert(self, data):
        self.rinsert(self.root, data)
    

    def inorder_rec(self, root):
        if root is None:
            return 
        self.inorder_rec(root.left)
        print(root.item)
        self.inorder_rec(root.right)
    def inorder(self):
        self.inorder_rec(self.root)

    
    # for printing item if treee
    def level_order(self):
        if self.root is None:
            return None
        
        result = []
        result.append(self.root)

        while result :
            root = result.popleft()

            if root.left:
                result.append(root.left)
            if root.right:
                result.append(root.right)
            print(root.item)

    def level_order1(self):
        final = [[self.root.item]]

        result = []
        result.append(self.root)
        
        while result:
            temp_node = []
            temp_item = []

            for root in result:
                if root.left:
                    temp_node.append(root.left)
                    temp_item.append(root.left.item)
                if root.right:
                    temp_node.append(root.right)
                    temp_item.append(root.right.item)

            result = temp_node

            if temp_item:
                final.append(temp_item)
        print(final)
    

    def delete(self, data):
        self.rdelete(self.root, data)
    
    def findMin(self, root):
        if root is None:
            return root

        while root.left:
            root = root.left

        return root.item
        

    def rdelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # finding successor
                root.item = self.findMin(root.right)
                root.right = self.rdelete(root.right, root.item)
        return root

            


T1 = BST(11)

T1.insert(8)
T1.insert(9)
T1.insert(10)
T1.insert(12)
T1.insert(-1)

T1.delete(7)

T1.level_order1()

print()
# T2.inorder()
