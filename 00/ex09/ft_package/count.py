def count_in_list(lst, item):
    """Count occurences in list"""
    res = 0
    for element in lst:
        if element == item:
            res += 1
    return (res)
