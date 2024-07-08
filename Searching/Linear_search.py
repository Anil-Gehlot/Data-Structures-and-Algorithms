
def linear_search(arr, key):
    for index in range(0, len(arr)-1):
        element = arr[index]

        if element == key :
            return index
    return "Not Found"

arr = arr = [23,4,235,345,324,56,3456,345,75,68,67978,9]

ans = linear_search(arr, 345)
print(ans)
