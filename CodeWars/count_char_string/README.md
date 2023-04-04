# **_Count characters in your string_**

## [**link**](https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python)

---

## **Descripotion**

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be

```
{'a': 2, 'b': 1}
```

What if the string is empty? Then the result should be empty object literal,

```
{}
```

## **Solution**

**Python**:

```python
# function to calculate count of letters in string
def count(s):
    letters_in_list = {}
    if len(s) == 0:
        return {}
    else:
        for i in s:
            letters_in_list[i] = letters_in_list.get(i,0)+1
    return letters_in_list
```
