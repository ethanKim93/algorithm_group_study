import sys
sys.stdin = open('input.txt')


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_len = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_len]:
                min_len = j
        arr[i], arr[min_len] = arr[min_len], arr[i]
    return arr


for tc in range(4):
    N = input()
    arr = []
    for i in range(len(N)):
        arr.append(int(N[i]))
    selection_sort(arr)
    if arr[0] == arr[1] == arr[2] or arr[0] + 2 == arr[1] + 1 == arr[2]:
        if arr[3] + 2 == arr[4] + 1 == arr[5] or arr[3] == arr[4] == arr[5]:
            print('#{} {} is BABY_GIN!'.format(tc + 1, N))
        else:
            print('#{} {} is not BABY_GIN!'.format(tc + 1, N))
    else:
        print('#{} {} is not BABY_GIN!'.format(tc + 1, N))