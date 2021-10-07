A = [11, 45, 23, 81, 28, 34]
B = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
C = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right = [], []

    for i in range(1,len(arr)):
        if pivot < arr[i]:
            right.append(arr[i])
        else:
            left.append(arr[i])

    left = quick_sort(left)
    right = quick_sort(right)

    return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(A))
print(quick_sort(B))
print(quick_sort(C))

# Output
# [11, 23, 28, 34, 45, 81]
# [8, 11, 17, 22, 22, 23, 34, 45, 81, 99]
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]