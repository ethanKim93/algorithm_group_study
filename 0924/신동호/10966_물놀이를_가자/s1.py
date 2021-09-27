import sys
sys.stdin = open('sample_input.txt')

from collections import deque

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     matrix = [[0] * M for _ in range(N)]
#     stack = deque()
#     dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     tot = 0
#     wat = 0
#
#     for i in range(N):
#         word = list(input())
#         for j in range(M):
#             if word[j] == 'W':
#                 matrix[i][j] = 1
#                 stack.append((i, j))
#                 wat += 1
#
#     while stack:
#         q0, q1 = stack.popleft()
#         for d in dxy:
#             w0 = q0 + d[0]
#             w1 = q1 + d[1]
#             if 0 <= w0 < N and 0 <= w1 < M and not matrix[w0][w1]:
#                 stack.append((w0, w1))
#                 matrix[w0][w1] = matrix[q0][q1] + 1
#                 tot += matrix[w0][w1]
#
#     print('#{} {}'.format(tc, tot - N * M + wat))

from collections import deque
# 좌표 읽을 때 이중 list 형태([w[0]])로는 시간 초과 되던데 단일 list(w[0])나 tuple 형태로 넣으면 통과됩니다
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    stack = deque()
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    tot = 0
    wat = 0

    for i in range(N):
        word = list(input())
        for j in range(M):
            if word[j] == 'W':
                matrix[i][j] = 1
                stack.append([i, j])
                wat += 1

    while stack:
        q0, q1 = stack.popleft()
        for d in dxy:
            w0 = q0 + d[0]
            w1 = q1 + d[1]
            if 0 <= w0 < N and 0 <= w1 < M and not matrix[w0][w1]:
                stack.append((w0, w1))
                matrix[w0][w1] = matrix[q0][q1] + 1
                tot += matrix[w0][w1]

    print('#{} {}'.format(tc, tot - N * M + wat))