import sys
sys.stdin = open("sample_input.txt")


def maze(start):
    queue = [start]

    while queue:
        n1, n2 = queue.pop(0)
        for i in range(4):
            a = n1 + di1[i]
            b = n2 + di2[i]
            if 0 <= a < N and 0 <= b < N:
                if not matrix[a][b] and not visited[a][b]:
                    queue.append([a, b])
                    visited[a][b] = visited[n1][n2] + 1
                if matrix[a][b] == 3:
                    return visited[n1][n2]
    return 0

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    di1 = [-1, 1, 0, 0] #상 하 좌 우
    di2 = [0, 0, -1, 1]
    start = [0, 0]
    flag = False
    for i in range(N):
        if flag:
            break
        for j in range(N):
            if matrix[i][j] == 2:
                start[0] = i
                start[1] = j
                flag = True
                break
    cnt = 0
    visited = [[0] * N for _ in range(N)]

    print('#{} {}'.format(tc, maze(start)))
