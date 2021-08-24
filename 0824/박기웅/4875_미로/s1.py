import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # find start point i, j
    for i in range(N):
        try:
            si, sj = i, miro[i].index(2)
            break
        except: pass

    # di, dj 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 인접 가능 배열
    adj = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if not miro[ni][nj] or miro[ni][nj] == 3:
                        adj[i][j].append((ni, nj))

    ans = 0
    stack = [(si, sj)]

    while stack:
        ni, nj = stack.pop()
        if miro[ni][nj] == 3:
            ans = 1
            break
        if visited[ni][nj]: continue

        visited[ni][nj] = 1
        for i,j in adj[ni][nj]:
            if not visited[i][j]:
                stack.append((i,j))

    print('#{} {}'.format(tc, ans))



