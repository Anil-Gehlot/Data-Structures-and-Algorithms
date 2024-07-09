

'''
Insertion sort divides the array into a sorted and an unsorted part. 
It takes elements from the unsorted part and inserts them into the correct position 
in the sorted part. The process repeats until the entire array is sorted.


complexity : O(n square)
'''


def insertion_sort(arr):

    for i in range(1, len(arr)):
        temp = arr[i]

        j = i-1

        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

arr = [23,4,235,345,324,56,3456,345,75,68,67978,9]
insertion_sort(arr)
print(arr)