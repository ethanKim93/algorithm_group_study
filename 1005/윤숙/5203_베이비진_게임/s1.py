#실패..

import sys
sys.stdin = open('input.txt')



def is_babyjin(p):
    tri = 0
    run = 0
    for i in range(0, 6, 3):
        if (p[i] == p[i + 1] == p[i + 2]):
            tri += 1
        if (p[i + 1] == p[i] + 1) and (p[i + 2] == p[i] + 2):
            run += 1


    return tri+run


def permutation(cnt, p, arr):
    global visited,maxv
    if cnt == n:
        return
    else:
        for j in range(n):
            if visited[j]:
                continue
            visited[j] = 1
            arr[cnt] = p[j]
            permutation(cnt + 1, p, arr)
            visited[j] = 0
            arr[cnt] = 0

    global maxv
    if maxv<is_babyjin(arr):
        maxv=is_babyjin(arr)
        print(maxv)

T = int(input())
for tc in range(1, T + 1):
    babygin = list(map(int, input().split()))
    p1 = []
    p1_arr = [0] * 6
    p2 = []
    p2_arr = [0] * 6
    for i in range(0, len(babygin), 2):
        p1.append(babygin[i])
        p2.append(babygin[i + 1])
    visited = [0] * (len(babygin))
    cnt = 0
    n = 6
    flag = 0
    maxv=0
    permutation(cnt, p1, p1_arr)
    maxv=0
    permutation(cnt, p2, p2_arr)
