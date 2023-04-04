# function to calculate count of letters in string
def count(s):
    letters_in_list = {}
    if len(s) == 0:
        return {}
    else:
        for i in s:
            letters_in_list[i] = letters_in_list.get(i,0)+1
    return letters_in_list