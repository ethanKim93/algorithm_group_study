import sys
sys.stdin = open('input.txt')

def prim():
    key = [float('inf')] * (N)
    visited = [0] * (N)
    key[0] = 0
    p = [-1]*N
    for _ in range(N):
        min_idx = -1
        min_value = float('inf')
        for i in range(N):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1

        for i in range(N):
            if not visited[i] and matrix[min_idx][i] < key[i]:
                key[i] = matrix[min_idx][i]
                p[i] = min_idx

    return sum(key)*E


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    matrix = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            matrix[i][j] = matrix[j][i] = (x[i] - x[j])**2 + (y[i] - y[j])**2

    print('#{} {}'.format(tc, round(prim())))