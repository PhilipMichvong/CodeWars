# function to calculate sum of 2 binary numbers
def binary_sum(a: int, b : int) -> bin:
    sum = bin(int(a)+ int(b))
    return sum[2:]