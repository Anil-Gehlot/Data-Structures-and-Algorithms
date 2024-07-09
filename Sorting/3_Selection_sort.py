


'''

Selection Sort divides the array into two parts: a sorted part and an unsorted part. 
It iterates through the unsorted part to find the minimum element and places it
at the end of the sorted part. This process repeats until the entire array is sorted.

complexity : O(n square)
'''

def selection_sort(arr):
    n = len(arr)

    for i in range(0, n-1):
        min_index = i

        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [23,4,235,345,324,56,3456,345,75,68,67978,9]
selection_sort(arr)
print(arr)