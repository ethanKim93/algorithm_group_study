import sys
sys.stdin = open("sample_input.txt")


def backtracking(matrix, N, row, g_min, l_min):
    if row == N:
        if l_min < g_min[0]:
            g_min[0] = l_min
        return

    if l_min > g_min[0]:
        return

    for col in range(N):
        if not visited[col]:
            visited[col] = 1
            backtracking(matrix, N, row + 1, g_min, l_min + matrix[row][col])
            visited[col] = 0
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_v =[N * 10]
    backtracking(matrix, N, 0, min_v, 0)
    print("#{} {}".format(tc, min_v[0]))