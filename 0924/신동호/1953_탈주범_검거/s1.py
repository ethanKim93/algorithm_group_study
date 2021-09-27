import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())

dr = [-1, 1, 0, 0] # 상하좌우
dc = [0, 0, -1, 1]

tunnel_type = [
    [],
    [0, 1, 2, 3],
    [0, 1],
    [2, 3],
    [0, 3],
    [1, 3],
    [1, 2],
    [0, 2],
]

tunnel_link = {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2,
}

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [[] for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    tot = 1
    time = 0
    for i in range(N):
        matrix[i] = list(map(int, input().split()))
    stack = deque()
    stack.append((R,C))
    visited[R][C] = 1
    while stack:
        q0, q1 = stack.popleft()
        for d in tunnel_type[matrix[q0][q1]]:
            w0 = q0 + dr[d]
            w1 = q1 + dc[d]
            if 0 <= w0 < N and 0 <= w1 < M and not visited[w0][w1] and (visited[q0][q1] <= L-1):
                flag = 0
                if tunnel_link.get(d) in tunnel_type[matrix[w0][w1]]:
                    stack.append([w0, w1])
                    visited[w0][w1] = visited[q0][q1] + 1
                    flag = 1
                if flag:
                    tot += 1

    print('#{} {}'.format(tc, tot))

