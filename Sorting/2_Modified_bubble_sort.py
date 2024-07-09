

"""
Best-case Time Complexity: O(n) when the array is already sorted 
(with the optimized version using the swapped flag).

"""

def modified_bubble_sort(arr):

    iteration = 0

    for i in range(0, len(arr)-1):
        flag = False
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],  arr[j+1] = arr[j+1],  arr[j]
                flag = True
            
            iteration += 1
        if flag == False:
            break
    print(iteration)

arr1 = [9, 1,2,3,4,5,6,7,8]
modified_bubble_sort(arr1)
print(arr1 )

