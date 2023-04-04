from array_dif import array_diff
from binary_sum import binary_sum
from is_square import *
from to_print import print_function
from find_outliners.find_outliners import find_outlier
def main():
    print_function("binnary sum",binary_sum(1,1))

    print_function("array diff", array_diff([1,2,3,4,5],[1,2,3,4]))

    print_function("is square", is_square(4))

    print_function("is square with math", is_square_math(4))

    print_function("find outliners", find_outlier([4,6,8,10,33]))

    
if __name__ == "__main__":

    main()
    