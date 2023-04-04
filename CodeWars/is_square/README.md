# **_You're a square!_**

## [**link**](https://www.codewars.com/kata/54c27a33fb7da0db0100040e)

---

## **Descripotion**

A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

```
In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
```

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

**Examples**

```
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
```

## **Solution**

**Python**:

```python
#function to show difference between two lists
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
```
