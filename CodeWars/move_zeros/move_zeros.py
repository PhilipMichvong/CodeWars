# function to move zeros in list to the end of list
def move_zeros(lst):
    non_zero = []
    zero = []
    for i in lst:
        if i == 0:
            zero.append(i)
        else:
            non_zero.append(i)
    final = non_zero + zero
    return final
