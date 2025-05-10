

def last_occurence(string,start_index,target_char, target_char_index):

    if start_index >= len(string):
        return target_char_index

    if string[start_index] == target_char:
        target_char_index = start_index

    return last_occurence(string,start_index+1,target_char, target_char_index)
    





string = "anaaThegangster"
start_index = 0 
target_char = "e"
target_char_index = "not found"

ans = last_occurence(string, start_index, target_char, target_char_index)
print(ans)