# **_Array.diff_**

## [**link**](https://www.codewars.com/kata/523f5d21c841566fde000009)

---

## **Descripotion**

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

```
array_diff([1,2],[1]) == [2]
```

If a value is present in b, all of its occurrences must be removed from the other:

```
array_diff([1,2,2,2,3],[2]) == [1,3]
```

## **Solution**

**Python**:

```python
#function to show difference between two lists
def array_diff(list1: list, list2:list) -> list:
    if list1.__eq__(list2):
        print("same lists")
        return []
    else:
        list3 = [x for x in list1 if x not in list2]
        return list3
```
