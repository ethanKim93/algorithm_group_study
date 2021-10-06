# Hoare - Partition
def Hoare_partition(arr, front, rear):
    p = arr[front]
    i = front
    j = rear
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[front], arr[j] = arr[j], arr[front]
    return j

# Lomuto - Partition
def Lomuto_partition(arr, front, rear):
    p = arr[rear]
    i = front - 1
    for j in range(front, rear):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[rear] = arr[rear], arr[i + 1]
    return i + 1

def quick_sort(arr, front, rear):
    if front < rear:
        s = Lomuto_partition(arr, front, rear)
        quick_sort(arr, front, s - 1)
        quick_sort(arr, s + 1, rear)
    return

a = [11, 45, 23, 81, 28, 34]
b = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
c = [1, 1, 1, 1, 1, 0, 0, 0, 0]


print(a)
quick_sort(a, 0, len(a) - 1)
print(a)

print(b)
quick_sort(b, 0, len(b) - 1)
print(b)

print(c)
quick_sort(c, 0, len(c) - 1)
print(c)