# **_Splits Strings_**

## [**link**](https://www.codewars.com/kata/515de9ae9dcfc28eb6000001)

---

## **Descripotion**

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('\_').

**_Examples_**:

```
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
```

## **Solution**

**Python**:

```python
# function to split string after every 2 letters
def split(s : str):

    if len(s)%2 != 0:
        s+="_"
# my own assumption, if there is a number in the string, i replace it with _
    for num in s:
        if num.isdigit():
            s = s.replace(num, "_")

    splited = [s[i:i+2] for i in range(0,len(s),2)]

    return splited
```
