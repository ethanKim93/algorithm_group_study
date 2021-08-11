import sys
sys.stdin = open('input.txt')


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


for tc in range(1, 11):
    T = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_list = []
    first_diagonal = 0
    second_diagonal = 0

    for i in range(len(arr)):
        total_row = 0
        for j in range(len(arr[i])):
            total_row += arr[i][j]
            if i == j:
                first_diagonal += arr[i][j]
        total_list.append(total_row)
        total_list.append(first_diagonal)

    for j in range(len(arr[0])):
        total_col = 0
        for i in range(len(arr)):
            total_col += arr[i][j]
        total_list.append(total_col)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == N-j:
                second_diagonal += arr[i][j]
    total_list.append(second_diagonal)

    result = selection_sort(total_list)[-1]
    print('#{} {}'.format(tc, result))
