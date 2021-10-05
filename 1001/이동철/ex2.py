"""
124783
667767
054060
101123
"""


def select_sort(ls, n):
    if n == len(arr):
        return ls
    else:
        min_n = n
        for j in range(n, len(arr)):
            if arr[j] < arr[min_n]:
                min_n = j
        arr[n], arr[min_n] = arr[min_n], arr[n]
        return select_sort(ls, n + 1)


for tc in range(4):
    N = input()
    arr = []
    for i in range(len(N)):
        arr.append(int(N[i]))
    select_sort(arr, 0)
    if arr[0] == arr[1] == arr[2] or arr[0] + 2 == arr[1] + 1 == arr[2]:
        if arr[3] + 2 == arr[4] + 1 == arr[5] or arr[3] == arr[4] == arr[5]:
            print('#{} {} ACCEPT!'.format(tc + 1, N))
        else:
            print('#{} {} DECLINE!'.format(tc + 1, N))
    else:
        print('#{} {} DECLINE!'.format(tc + 1, N))

