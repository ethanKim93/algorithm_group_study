a = [11,45,23,81,28,34]

def partition(a, l, r):
    p = a[l]
    i = l
    j = r
    while i <= j:
        while i <= j and a[i] <= p:
            i += 1
        while i <= j and a[j] >= p:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    return j

def quickSort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quickSort(a, l, s-1)
        quickSort(a, s+1, r)

quickSort(a, 0, 5)
print(a)