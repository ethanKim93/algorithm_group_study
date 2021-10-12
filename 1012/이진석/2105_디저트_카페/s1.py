import sys

sys.stdin = open('sample_input.txt')

delta = [(-1, 1), (1, 1), (1, -1), (-1, -1)]  # 1시, 5시, 7시, 11시


# def search(row, col):
#     global max_visit
#     stack.append((row, col))
#     visited[row] |= (1 << col)
#     while stack:
#         now = stack.pop()
#         r, c = now[0], now[1]
#         for d in range(4):
#             nr = r + delta[d][0]
#             nc = c + delta[d][1]
#             if 0 <= nr < N and 0 <= nc < N and not visited[nr] & (1 << nc) and cafe[nr][nc] not in stack:
#                 visited[nr] |= (1 << nc)
#                 stack.append((nr, nc))
#
#
def search(r, c, start, dir):
    global max_visit
    if dir == 4 and (r, c) == start:
        if len(stack) > max_visit:
            max_visit = len(stack)
            return

    nr, nc = r + delta[dir % 4][0], c + delta[dir % 4][1]
    # if 0 <= nr < N and 0 <= nc < N and not visited[nr] & (1 << nc) and cafe[nr][nc] not in stack:
    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and cafe[nr][nc] not in stack:
        # visited[nr] |= (1 << nc)
        visited[nr][nc] = 1
        stack.append(cafe[nr][nc])
        if 0 <= nr + delta[dir % 4][0] < N and 0 <= nc + delta[dir % 4][1] < N:
            search(nr, nc, start, dir)
        else:
            search(nr, nc, start, dir + 1)
        stack.pop()
        # visited[nr] &= ~(1 << nc)
        visited[nr][nc] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    max_visit = -1
    # visited = [(1 << N)] * N
    visited = [[0] * N for _ in range(N)]
    delta_v = [0, 0, 0, 0]
    for i in range(N - 1):
        for j in range(N - 2):
            search(i, j, (i, j), 0)
            stack.clear()
    print(max_visit)
# # delta
# dr = (1, 1, -1, -1)
# dc = (1, -1, -1, 1)


# dfs
def dfs(r, c, dir):
    global start, max_val
    if dir == 3 and (r, c) == start:
        # 먹은 디저트 수 세기
        val = 0
        for dessert in desserts:
            if dessert:
                val += 1
        # 최대값 갱신
        if val > max_val:
            max_val = val

    if r < 0 or r >= N or c < 0 or c >= N or desserts[arr[r][c]]:
        return

    desserts[arr[r][c]] = 1

    # 현재 방향으로 이동
    nr1, nc1 = r + dr[dir], c + dc[dir]
    dfs(nr1, nc1, dir)
    # 다음 방향으로 이동
    if dir != 3:
        nr2, nc2 = r + dr[dir + 1], c + dc[dir + 1]
        dfs(nr2, nc2, dir + 1)

    # 원상복구
    desserts[arr[r][c]] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = -1
    desserts = [0] * 101

    for i in range(N - 1):
        for j in range(1, N - 1):
            start = (i, j)
            dfs(i, j, 0)

    print('#{} {}'.format(tc, max_val))