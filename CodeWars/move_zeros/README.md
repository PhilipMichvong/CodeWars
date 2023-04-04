# **_Moving Zeros To The End!_**

## [**link**](https://www.codewars.com/kata/52597aa56021e91c93000cb0/python)

---

## **Descripotion**

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

```
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```

## **Solution**

**Python**:

```python
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

```
