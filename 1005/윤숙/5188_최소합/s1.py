import sys

sys.stdin = open('input.txt')


def FindMinSum(px, py):
    global total, minV
    if minV < total:
        return
    if px == N - 1 and py == N - 1:
        if minV > total:
            minV = total
            return
    for i in range(2):
        cx = px + delx[i]
        cy = py + dely[i]
        if 0 <= cx < N and 0 <= cy < N:
            if visited[cx][cy] == 0:
                visited[cx][cy] = 1
                total += arr_chart[cx][cy]
                FindMinSum(cx, cy)
                visited[cx][cy] = 0
                total -= arr_chart[cx][cy]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr_chart = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    minV = 9999999999
    # 우, 하
    delx = [0, 1]
    dely = [1, 0]
    px = 0;
    py = 0
    total = arr_chart[px][py]
    visited[px][py] = 1
    FindMinSum(px, py)
    print('#{} {}'.format(tc, minV))
