def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    original_set.difference_update(elements_to_remove)
    return original_set
print(remove_elements({1, 2, 3, 4}, [2, 3]))