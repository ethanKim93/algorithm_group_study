import sys
sys.stdin = open('sample_input.txt')

def dfs(i, j):
    way = []
    visited[i][j] = 1


    # 상 우 하 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]


    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if (0 <= ni < N) and (0 <= nj < N):
            if (miro[ni][nj] != '1') and (visited[ni][nj] == 0):
                way.append([ni, nj])

    for w in way:
        dfs(*w)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = []
    for _ in range(N):
        miro.append(input())

    visited = [[0]*N for _ in range(N)]

    # 시작점
    i, j = 0, 0
    for a in range(len(miro)):
        for b in range(len(miro)):
            if miro[a][b] == '2':
                i = a
                j = b

    # 끝점
    end_i, end_j = 0, 0
    for a in range(len(miro)):
        for b in range(len(miro)):
            if miro[a][b] == '3':
                end_i = a
                end_j = b

    dfs(i, j)
    print('#{} {}'.format(tc, visited[end_i][end_j]))