import sys
sys.stdin = open('sample_input.txt')

# 최소 연산 횟수 -> BFS
def bfs(N, cnt):
    visited[N] = 1
    Q = [(N, cnt)]
    for n, c in Q:
        if n == M: return c
        for nn in [n-1, n+1, 2*n, n-10]:    # 연산의 종류
            if nn > INF or nn<0: continue   # 안되는 경우
            if not visited[nn]:
                visited[nn] = 1
                Q.append((nn, c+1))
                   
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    INF = 1000000
    min_cnt = INF
    visited = [0]*(INF+1)
    min_cnt = bfs(N,0)
        
    print('#{} {}'.format(tc, min_cnt))