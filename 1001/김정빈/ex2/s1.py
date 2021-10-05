"""
6자리 숫자에 대해서 완전 검색을 적용해서 baby-git을 검사해보시오
1, 2, 4, 7, 8, 3
6, 6, 7, 7, 6, 7
0, 5, 4, 0, 6, 0
1, 0, 1, 1, 2, 3
"""


def isbabygin(p):
    tri, run = 0, 0
    for i in range(0, 6, 3):
        if p[i]+2 == p[i+1]+1 == p[i+2]:
            run += 1
        elif p[i] == p[i+1] == p[i+2]:
            tri += 1
    if tri + run == 2:
        return True
    return False


def perm(arr, n, k):
    global cnt, bg
    if k == n:
        cnt += 1
        if isbabygin(arr):
            bg += 1
            # print(p)
        return
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr, n, k+1)
            arr[k], arr[i] = arr[i], arr[k]


arrs = [[1, 0, 1, 1, 2, 3], [6, 6, 7, 7, 6, 7], [0, 5, 4, 0, 6, 0], [1, 0, 1, 1, 2, 3]]
for arr in arrs:
    cnt, bg = 0, 0
    perm(arr, 6, 0)
    print('총 {}개의 순열 중 {}개의 babygin을 발견했습니다.'.format(cnt, bg))