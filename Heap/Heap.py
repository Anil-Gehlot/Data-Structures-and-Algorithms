# Max Heap
import math
class Heap:
    def __init__(self):
        self.heap = []
    

    def insert(self, data):
        self.heap.append(data)

        index = len(self.heap)-1

        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index] :
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    #  root only
    def delete(self):

        if len(self.heap) == 0:
            return


        self.heap[0] = self.heap.pop()
        
        index = 0 
        while index < len(self.heap)//2:
            left = self.heap[(2*index)+1] if (2*index)+1 < len(self.heap) else -math.inf
            right = self.heap[(2*index)+2] if (2*index)+2 < len(self.heap) else -math.inf

            #  left > right ? (2*index)+1 : (2*index)+2
            larger = (2*index)+1 if  left > right  else (2*index)+2

            if self.heap[larger] > self.heap[index]:
                self.heap[larger], self.heap[index] = self.heap[index], self.heap[larger]
                index = larger
            else:
                break
   

    def heapify(self, index):
        n = len(self.heap)
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)

    def print_heap(self):
        print(self.heap)

    def build_heap(self):
        n = len(self.heap)
        for ind in range(n//2, -1, -1):
            self.heapify(ind)

H = Heap()
# H.insert(1)
# H.insert(2)
# H.insert(3)
# H.insert(4)
# 
# H.insert(8)
# H.insert(7)
# H.insert(6)
# H.insert(9)
H.build_heap()
H.print_heap()


