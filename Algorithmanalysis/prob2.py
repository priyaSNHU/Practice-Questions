def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))



lst = ['j', 'z', 'v', 'p', 'b', 'j', 'b', 'c', 'd', 'e', 'f', 's', 'r', 'j']
print(quicksort(lst))
