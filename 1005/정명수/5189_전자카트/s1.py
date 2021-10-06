import sys
sys.stdin = open('input.txt')

def small(now,sums,cnt,visited):
    global min_consume
    if cnt == N-1:
        sums += arr[now][0]
        if min_consume > sums:
            min_consume = sums
        return
    else:
        if min_consume < sums:
            return
        for x in range(1,N):
            if not visited[x] and x != now:
                visited[x]=1
                small(x,sums+arr[now][x],cnt+1,visited)
                visited[x]=0



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_consume = 1000000
    visited = [0]*(N+1)
    small(0,0,0,visited)
    print('#{} {}'.format(tc,min_consume))
