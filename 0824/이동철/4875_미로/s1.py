import sys
sys.stdin = open('input.txt')


def ok(process):
    return 0 <= process[0] < N and 0 <= process[1] < N and process not in visited


def nextarea(process):
    return ok(process) and miro[process[0]][process[1]] == 0


def end(process):
    return ok(process) and miro[process[0]][process[1]] == 3


def dfs(start):
    global result
    visited.append(start)
    for i in range(4): #상하좌우
        if result == 0:
            process = (start[0] + direction[i][0], start[1] + direction[i][1])
            if end(process):
                result = 1
                return
            elif nextarea(process):
                dfs(process)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = []
    start = 0

    for r in range(N):
        for c in range(N):
            if miro[r][c] == 2:
                start = (r, c)

    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
    result = 0
    dfs(start)

    print('#{} {}'.format(tc, result))
