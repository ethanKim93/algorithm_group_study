arr = [11, 54, 12, 74, 23, 44]
R = len(arr)

cnt = 0
minidx = arr[1]


def selection_sort(cnt):
    if cnt + 1 == R:
        return
    for i in range(R):
        if arr[cnt] < arr[cnt + 1]:
            minidx = cnt
            arr[cnt + 1], arr[minidx] = arr[minidx], arr[cnt + 1]
            selection_sort(cnt + 1)


selection_sort(cnt)
print(arr)
