
"""
The time complexity of a binary search algorithm is  O(logn). 
This is because the algorithm repeatedly divides the search range in half, 
reducing the problem size by a factor of two with each iteration.


condition : array must be sorted.
"""

def binary_search(arr, key):

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] > key:
            end = mid - 1

        elif arr[mid] < key:
            start = mid + 1

    return "Not Found"


arr = [4, 9, 23, 56, 68, 75, 235, 324, 345, 345, 3456, 67978]

print(binary_search(arr, 9))        # 1
print(binary_search(arr, 10))       # Not Found