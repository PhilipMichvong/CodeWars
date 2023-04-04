def find_outlier(integers) -> int:

    list_of_numbers_odd = []
    list_of_numbers_even = []

    for i in integers:

        if i%2 == 0:
            list_of_numbers_even.append(i)
        else:
            list_of_numbers_odd.append(i)
        
    if len(list_of_numbers_even) == 1:
        return int(list_of_numbers_even.pop())
    
    else:
        return int(list_of_numbers_odd.pop())