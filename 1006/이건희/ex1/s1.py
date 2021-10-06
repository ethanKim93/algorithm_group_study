# alist = [11, 45, 23, 81, 28, 34]
alist = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
# alist = [1,1,1,1,1,0,0,0,0,0]

def quicksort(li, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= end and start < right:
        while left <= end and li[left] <= li[pivot]:
            left += 1
        while right > start and li[right] >= li[pivot]:
            right -= 1

        if left > right:
            li[pivot], li[right] = li[right], li[pivot]
        else:
            li[left], li[right] = li[right], li[left]

    quicksort(li, start, right-1)
    quicksort(li, right+1, end)


quicksort(alist,0,len(alist)-1)
print(alist)

# Pass