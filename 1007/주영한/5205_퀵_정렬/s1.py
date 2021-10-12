def partition(arr, start, end):
    p = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(arr, start, end):
    if end <= start:
        return
    s = partition(arr, start, end)
    quick_sort(arr, start, s - 1)
    quick_sort(arr, s + 1, end)    
    return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
    print("#{} {}".format(tc, arr[N//2]))