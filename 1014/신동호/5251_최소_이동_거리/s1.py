import sys
sys.stdin = open('sample_input.txt')

def Dijkstra(s, N):
    U = [0] * (N+1)
    U[s] = 1
    for v in range(N+1):
        D[v] = A[s][v]
    
    while sum(U) != N:
        min_w = 987654321
        for i in range(N+1):
            if min_w > D[i] and not U[i]:
                min_w = D[i]
                w = i
        U[w] = 1

        for v in range(N+1):
            D[v] = min(D[v], D[w]+A[w][v])


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    A = [[987654321] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        A[s][e] = w
    D = [0] * (N+1)
    Dijkstra(0, N)
    print('#{} {}'.format(tc, D[N]))