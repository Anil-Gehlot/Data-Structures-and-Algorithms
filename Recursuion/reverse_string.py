

def reverse(string, op_string, last_index):

    # base condition
    if last_index < 0:
        return op_string

    # processing
    op_string += string[last_index]

    # recursive relation
    return reverse(string, op_string, last_index-1)





string = "anil"
op_string = ""
last_index = len(string)-1
ans = reverse(string, op_string, last_index)
print(ans)