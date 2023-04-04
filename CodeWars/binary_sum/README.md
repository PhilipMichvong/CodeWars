# **_Binary Addition_**

## [**link**](https://github.com/PhilipMichvong/CodeWars/blob/main/CodeWars/assets/banner.jpg?raw=true)

---

## **Descripotion**

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

**Examples:**

```test
1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
```

## **Solution**

**Python**:

```python
# function to calculate sum of 2 binary numbers
def binary_sum(a: int, b : int) -> bin:
    sum = bin(int(a)+ int(b))
    return sum[2:]
```
