
"""
Bubble Sort Explained
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list to be sorted,
compares adjacent items, and swaps them if they are in the wrong order. 
The process is repeated until the list is sorted.

complexity : O(n square)
"""


def bubble_sort(arr):

    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    

arr = [23,4,235,345,324,56,3456,345,75,68,67978,9]
bubble_sort(arr)
print(arr)

