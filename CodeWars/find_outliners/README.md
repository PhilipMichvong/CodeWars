# **_Find The Parity Outlier_**

## [**link**](https://www.codewars.com/kata/5526fc09a1bbd946250002dc)

---

## **Descripotion**

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

**Examples**

```
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)
```

```
[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
```

## **Solution**

**Python**:

```python
# function to calculate sum of 2 binary numbers
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
```
