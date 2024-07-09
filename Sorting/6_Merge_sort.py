'''

Merge Sort Algorithm
Merge Sort is a stable, comparison-based sorting algorithm that follows 
the divide-and-conquer paradigm. It works by recursively splitting the array 
into two halves, sorting each half, and then merging the sorted halves back together.

Time Complexity : O(nlogn) in all cases (best, average, worst).
space complexity: O(n) due to the additional space needed for merging the sorted sub-arrays.

'''




def merge_sort(arr):

    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2

    # Recursively sort the two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge_two_sorted_list(left_sorted, right_sorted)



def merge_two_sorted_list(list1, list2):
    merged_list = []

    i = j = 0

    # Compare elements from both lists and merge them in sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements from list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Append remaining elements from list2, if any\
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list



arr = [23,4,235,345,324,56,3456,345,75,68,67978,9]
print(merge_sort(arr))