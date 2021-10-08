import sys
sys.stdin = open('input.txt')


def FindMinSum(s, total):
    global  minV
    if minV < total:
        return

    if s==N:
        if minV > total:
            minV = total
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            FindMinSum(s+1, total+ arr[s][j])
            visited[j] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minV = 9999999999
    total=0
    s = 0
    FindMinSum(s,total)
    print('#{} {}'.format(tc, minV))
