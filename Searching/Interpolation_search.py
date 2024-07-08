
"""
Interpolation search is an improved variant of binary search, 
optimized for uniformly distributed datasets(differnce between each neighbour is same).

"""

def interpolation_search(arr, key):
    low = 0
    high = len(arr)-1

    # formula of interpolation search
    pos = low + ((key - arr[low]) * (high - low) // (arr[high] - arr[low]))
    
    if pos <= high and  arr[pos] == key:
        return pos
    return "NOT FOUND"


arr = [1,3,5,7,9,11,13,15,17]

print(interpolation_search(arr, 13))        # 6