import sys
sys.stdin = open('input.txt')

# 미완성
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    cnt = 1
    a = i = j = 1

    if a % 2:
        for i in range(len(arr)):
            a[i][j] = cnt
            cnt += 1
        a += 1
    else:
        for j in range(len(arr)):

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = cnt
            cnt += 1