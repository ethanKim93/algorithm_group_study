# alist = [11, 45, 23, 81, 28, 34]
# alist = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
alist = [1,1,1,1,1,0,0,0,0,0]

def quicksort(li):
    if len(li) <= 1:
        return li

    pivot = li[0]
    remainder = li[1:]

    left = [x for x in remainder if x <= pivot]
    right = [x for x in remainder if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort(alist))
# Pass