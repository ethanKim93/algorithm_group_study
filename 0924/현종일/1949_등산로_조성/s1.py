import sys
sys.stdin = open("sample_input.txt")

def dfs(r, c, now, cnt, flag):
    visited[r][c] = 1
    global ans
    if cnt > ans:
        ans = cnt

    for dir in range(4):
        nr, nc = r+dr[dir], c+dc[dir]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if now > field[nr][nc]:
                dfs(nr, nc, field[nr][nc], cnt + 1, flag)
            elif flag and now > field[nr][nc] - K:
                dfs(nr, nc, field[r][c]-1, cnt + 1, False)

    visited[r][c] = 0



T = int(input())
dr = [-1, 1, 0, 0] #상 하 좌 우
dc = [0, 0, -1, 1]

for tc in range(1,T+1):
    N, K = map(int, input().split())
    field = []
    visited = []
    max_height = 0
    max_loc = []
    result = 1
    ans = 0
    for i in range(N):
        arr = list(map(int, input().split()))
        field.append(arr)
        visited.append([0] * N)
        for j in range(N):
            if field[i][j] > max_height:
                max_height = field[i][j]
                max_loc = []
                max_loc.append([i, j])
            elif field[i][j] == max_height:
                max_loc.append([i, j])

    for loc in max_loc:
        r = loc[0]
        c = loc[1]
        dfs(r, c, max_height, result, True)

    print("#{} {}".format(tc, ans))




