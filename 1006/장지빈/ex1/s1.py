a = [11, 45, 23, 81, 28, 34]
a1 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
a2 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

def partition(a, l, r):
    p = a[l]
    i, j = l, r
    while i <= j:
        while i <= j and a[i] <= p:
            i += 1
        while i <= j and a[j] >= p:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def quick_sort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quick_sort(a, l, s-1)
        quick_sort(a, s+1, l)