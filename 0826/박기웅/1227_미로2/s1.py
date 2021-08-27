import sys
sys.stdin = open("input.txt")

def dfs(S):
    stack.append(S)

    while stack:
        i, j = stack.pop()
        visited[S[0]][S[1]] = 1
        if miro[i][j] == '3':
            return 1

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if ni in range(100) and nj in range(100) and not visited[ni][nj]:
                if miro[ni][nj] == '0' or miro[ni][nj] == '3':
                    stack.append([ni, nj])
                    visited[ni][nj] = 1
    return 0

for _ in range(1, 11):
    tc = input()
    miro = [list(input()) for _ in range(100)]
    stack = []
    visited = [[0]*100 for _ in range(100)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상, 하, 좌, 우

    for i in range(100):
        for j in range(100):
            if miro[i][j] == '2':
                S = [i, j]

    print('#{} {}'.format(tc, dfs(S)))
