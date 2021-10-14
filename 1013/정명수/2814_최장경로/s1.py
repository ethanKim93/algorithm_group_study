import sys
sys.stdin = open('input.txt')

def dfs(n,cnt):
    global answer
    answer = max(cnt,answer)
    for i in adj_list[n]:
        if not visited[i]:
            visited[i] = 1
            dfs(i,cnt+1)
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    adj_list = [[] for _ in range(N+1)]

    for _ in range(M):
        a,b = map(int,input().split())
        adj_list[b].append(a)
        adj_list[a].append(b)
    answer = 0
    for i in range(N+1):
        visited = [0] * (N + 1)
        visited[i]=1
        dfs(i,1)
        visited[i]=0
    print('#{} {}'.format(tc,answer))


