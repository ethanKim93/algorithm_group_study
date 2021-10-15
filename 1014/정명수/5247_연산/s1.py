import sys
sys.stdin = open('input.txt')

def BFS(n):
    global answer
    q = [n]
    while q:
        x = q.pop(0)
        if x == M:
            answer = dist[x]
            break
        for nx in (x-1,x+1,x-10,2*x):
            if 0 < nx <= M*2 and not dist[nx]:
                dist[nx] = dist[x]+1
                q.append(nx)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    answer = 10000
    dist = [0]*(2*M) # 각 인덱스까지 도달하는데 걸리는 횟수를 기록
    BFS(N)
    print('#{} {}'.format(tc,answer))