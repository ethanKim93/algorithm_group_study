import sys
sys.stdin = open("input.txt")
#5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
def dfs(st, tot ,cnt):
    global res
    if tot > res:
        return

    # if st == n-1: # 끝까지 도착
    if cnt == n-1:
        tot += arr[st][0] # 처음으로 되돌아가고 그 값을 더함
        if tot <= res: # 다했으니까 최소값이면 답에 저장
            res = tot
        return

    for i in range(1, n):
        if not visited[i] and i != st:
            visited[i] = 1
            dfs(i, tot+arr[st][i], cnt+1)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    res = 99999
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, res))