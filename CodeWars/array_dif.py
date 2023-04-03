#function to show difference between two lists
def array_diff(list1: list, list2:list) -> list:
    if list1.__eq__(list2):
        print("same lists")
        return []
    else:
        list3 = [x for x in list1 if x not in list2]
        return list3