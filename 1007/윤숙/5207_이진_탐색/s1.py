#테스트케이스 일부만 정답
import sys
sys.stdin = open('input.txt')


def divide(l, r):
    global flag

    if l > r:
        return
    i = l
    j = r
    mid = (i + j) // 2
    if find == arr_N[mid]:
        flag+=1
        return

    if find < arr_N[mid]:
        divide(i, mid - 1)

    elif find > arr_N[mid]:
        divide(mid + 1, j)




T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # A
    arr_N = sorted(list(map(int, input().split())))
    # B
    arr_M = list(map(int, input().split()))
    flag = 0
    l = 0
    r = len(arr_N) - 1
    for i in range(M):
        find = arr_M[i]
        result=1
        divide(l, r)
    print('#{} {}'.format(tc,flag ))
