import sys
sys.stdin = open('sample_input.txt')

def dfs(v, dist, k, height):
    global max_dist
    visited[v[0]][v[1]] = 1
    for d in dxy:
        w = [v[0] + d[0], v[1] + d[1]]
        if 0 <= w[0] < N and 0 <= w[1] < N and not visited[w[0]][w[1]]:
            if matrix[w[0]][w[1]] < height:
                dfs(w, dist+1, k, matrix[w[0]][w[1]])
            elif not k and matrix[w[0]][w[1]] - height < K:
                dfs(w, dist+1, 1, height-1)
            elif max_dist < dist:
                max_dist = dist
    visited[v[0]][v[1]] = 0

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [[] for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(N):
        matrix[i] = list(map(int, input().split()))
    max_h = 0
    ind_h= []
    max_dist = 0
    for x in range(N):
        for y in range(N):
            if matrix[x][y] > max_h:
                max_h = matrix[x][y]
                ind_h = [[x, y]]
            elif matrix[x][y] == max_h:
                ind_h += [[x, y]]
    for ind in ind_h:
        dfs(ind, 1, 0, max_h)
    print('#{} {}'.format(tc, max_dist))

