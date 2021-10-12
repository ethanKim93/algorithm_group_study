import sys
sys.stdin = open("sample_input.txt")

def dfs(n, tot):
    global res
    if tot > res:
        return
    if n == N:
        if tot < res:
            res = tot
        return
    for i in range(N):
        if seled[i] == 0:
            seled[i] = 1
            dfs(n+1, tot+value[n][i])
            seled[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    value = [list(map(int,input().split())) for _ in range(N)]
    seled = [0]*N
    res = 9999
    dfs(0,0)
    print('#{} {}'.format(tc, res))