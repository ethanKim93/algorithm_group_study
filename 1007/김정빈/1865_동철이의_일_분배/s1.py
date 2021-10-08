import sys
sys.stdin = open("input.txt")
#1865_동철이의_일_분배
#4366_정식이의_은행업무
def dfs(n, tot):
    global res
    if n == N:
        if tot > res:
            res = tot
        return
    if tot <= res:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, tot*arr[n][i])
            visited[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(lambda x:int(x)/100,input().split())) for _ in range(N)]
    visited = [0]*N
    res = 0
    dfs(0,1)
    print('#{} {:.6f}'.format(tc, res*100))