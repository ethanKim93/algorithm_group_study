import sys
sys.stdin = open("sample_input.txt")

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

pipes_from = {
    1: [True, True, True, True],
    2: [True, True, False, False],
    3: [False, False, True, True],
    4: [True, False, False, True],
    5: [False, True, False, True],
    6: [False, True, True, False],
    7: [True, False, True, False]
}

pipes_to = {
    1: [True, True, True, True],
    2: [True, True, False, False],
    3: [False, False, True, True],
    4: [False, True, True, False],
    5: [True, False, True, False],
    6: [True, False, False, True],
    7: [False, True, False, True]
}

def cnt():
    global N, M
    result = 0
    for row in range(N):
        for col in range(M):
            if visited[M * row + col]:
                result += 1
    return result

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    fields = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N * M)]

    front = -1
    rear = 0
    queue = [0] * (N * M)
    queue[rear] = M * R + C
    visited[M * R + C] = 1

    while front != rear:
        front += 1
        row = queue[front] // M
        col = queue[front] % M
        # idx = 0 ~ 3 : 상하좌우
        for idx, direction in enumerate(directions):
            if pipes_from[fields[row][col]][idx]:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row < N and 0 <= new_col < M and fields[new_row][new_col] and not visited[M * new_row + new_col] and pipes_to[fields[new_row][new_col]][idx]:
                    if 1 <= visited[M * row + col] < L:
                        visited[M * new_row + new_col] = visited[M * row + col] + 1
                        rear += 1
                        queue[rear] = M * new_row + new_col
    print("#{} {}".format(tc, cnt()))
