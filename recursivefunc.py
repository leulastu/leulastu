def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = (len(list)) // 2
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid + 1:], target)
            else:
                return recursive_binary_search(list[:mid], target)


def verify(result):
    print("target found :", result)

"""use the followign condition to test the output will be"target found : True" if the number exist in the list"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = recursive_binary_search(numbers, 9)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
