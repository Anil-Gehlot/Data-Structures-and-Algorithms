

"""

Quick Sort Algorithm: 

** quick sort is just made of two things:
1. partitions logic
2. recursion logic

Quick Sort is a highly efficient sorting algorithm and is 
based on the divide-and-conquer approach. It works by selecting 
a 'pivot' element from the array and partitioning the other elements
into two sub-arrays, according to whether they are less than or greater 
han the pivot. The sub-arrays are then sorted recursively.

Best Case: O(nlogn)
Average Case: O(nlogn)
Worst Case: O(n square )

"""


# with extra space 
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
     # Select the first element as the pivot
    pivot = arr[0]
    smaller, equal, larger = [], [], []

    for num in arr:
        if num == pivot:
            equal.append(num)
        elif num < pivot:
            smaller.append(num)
        else:
            larger.append(num)

    return quick_sort(smaller) + equal + quick_sort(larger)



arr = [23,4,235,345,324,56,3456,345,75,68,67978,9]
print(quick_sort(arr))







# in place quick sort 
def quick_sort_in_place(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort_in_place(arr, low, p - 1)
        quick_sort_in_place(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
