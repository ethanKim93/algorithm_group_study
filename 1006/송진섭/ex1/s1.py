def partition(a_list, l, r):
    pivot = a_list[l]
    i, j = l, r
    while i <= j:
        while i <= j and a_list[i] <= pivot:
            i += 1
        while i <= j and a_list[j] >= pivot:
            j -= 1
        if i < j:
            a_list[i], a_list[j] = a_list[j], a_list[i]
    a_list[l], a_list[j] = a_list[j], a_list[l]
    return j


def quick_sort(a_list, l, r):
    if l < r:
        s = partition(a_list, l, r)
        quick_sort(a_list, l, s-1)
        quick_sort(a_list, s+1, r)


a = [5, 6, 9, 1, 5, 3, 2]
quick_sort(a, 0, 6)
print(a)