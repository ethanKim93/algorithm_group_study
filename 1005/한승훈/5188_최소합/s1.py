import sys
sys.stdin = open('sample_input.txt')


def dfs(i, j, min_ans):
    global ans
    min_ans += matrix[i][j]
    if ans < min_ans:
        return
    if i == j == N-1:
        ans = min_ans
        return

    for idx in range(2):
        nx, ny = i + dir[idx][0], j + dir[idx][1]
        if nx < N and ny < N:
            dfs(nx, ny, min_ans)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 100000
    dir = [[0,1], [1,0]]
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, ans))
