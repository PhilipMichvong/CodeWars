from array_diff.array_dif import array_diff
from binary_sum.binary_sum import binary_sum
from is_square.is_square import *
from to_print import print_function
from find_outliners.find_outliners import find_outlier
from move_zeros.move_zeros import move_zeros
from count_char_string.count import count
from rot13.rot13 import rot13
from split_strings.split import split
from to_jaden_case.jaden import to_jaden_case

# def nb_year(p0, percent, aug, p):
    
#     years_to_reach = 0
#     finall_percent = percent/100
#     print(finall_percent)
#     while p>=p0:
        
#         p0 = p0 + finall_percent*p0 + aug
#         p0 = round(p0)
#         years_to_reach+=1

#     return years_to_reach

def score(dice) -> int:
    from collections import Counter
    points = {1:1000, 6:600, 5:500, 4:400, 3:300, 2:200}
    dices = Counter(dice)
    total_points= 0
    for num, value in dices.items():
        if value >=3:
            total_points += points[num] * (value//3) # floor division
        if num == 5:
            total_points += 50 * (value%3)
        elif num == 1:
            total_points += 100 * (value%3)
    return int(total_points)


def main():
 
    score([1,1,1,3,4])

if __name__ == "__main__":

    main()
    