import sys
sys.stdin = open('input.txt')
from pprint import pprint

for tc in range(10):
    T = input()
    max_arr = 0

    arr = [list(map(int, input().split())) for _ in range(100)]
    L = len(arr)
    L2 = len(arr)
    for i in range(L):

        sum_arr = 0
        for j in range(L2):
            sum_arr += arr[i][j]
            if sum_arr >= max_arr:
                max_arr = sum_arr

        sum_arr = 0
        for a in range(L2):
            sum_arr += arr[a][i]
            if sum_arr >= max_arr:
                max_arr = sum_arr
# 행 / 열 순회


    for x in range(L2):
        sum_arr = 0
        sum_arr += arr[x][x]
        if sum_arr >= max_arr:
            max_arr = sum_arr
# 우하향 직선 순회

    for y in range(L2):
        sum_arr = 0
        for z in range(L2-1, -1, -1):
            sum_arr += arr[y][z]
            if sum_arr >= max_arr:
                max_arr = sum_arr
# 좌하향 직선 순회
    print('#{} {}'.format(T, max_arr))