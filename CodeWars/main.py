from array_diff.array_dif import array_diff
from binary_sum.binary_sum import binary_sum
from is_square.is_square import *
from to_print import print_function
from find_outliners.find_outliners import find_outlier
from move_zeros.move_zeros import move_zeros
from count_char_string.count import count
from rot13.rot13 import rot13
from split_strings.split import split
def split(s : str):
    
    if len(s)%2 != 0: 
        s+="_"

    for num in s:
        if num.isdigit():
            s = s.replace(num, "_")
    
    splited = [s[i:i+2] for i in range(0,len(s),2)]

    return splited

def main():
    
    print_function("binnary sum",binary_sum(1,1))

    print_function("array diff", array_diff([1,2,3,4,5],[1,2,3,4]))

    print_function("is square", is_square(4))

    print_function("is square with math", is_square_math(4))

    print_function("find outliners", find_outlier([4,6,8,10,33]))
    
    print_function("move zeros", move_zeros([0,0,8,10,33]))
    
    print_function("Count characters in your string",  count("sasasadadasaasadadad"))

    print_function("Root_13", rot13("very very secret"))
 
    print_function("split string",split("123testtest"))

if __name__ == "__main__":

    main()
    