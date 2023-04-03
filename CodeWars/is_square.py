import math
# fucntion to check if number in parameter is square with math library
def is_square_math(n) -> bool:
    test = math.sqrt(n)
    test2 = int(test)
    return test == test2
# fucntion to check if number in parameter is square
def is_square(n) -> bool:
    if (n < 0):
        return False
    x = n // 2
    seen = set([x])
    while x * x != n:
      x = (x + (n // x)) // 2
      if x in seen: return False
    return True