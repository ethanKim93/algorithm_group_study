import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    drx = [0, 1, 0, -1]
    dry = [1, 0, -1, 0]
    matrix = [[0]*N for _ in range(N)]
    now_x = 0
    now_y = -1
    d=0
    for n in range(1, N*N+1):
        now_x += drx[d%4]
        now_y += dry[d%4]
        if now_x >= N or now_y >= N or now_x < 0 or now_y < 0 or matrix[now_x][now_y] != 0:
            now_x -= drx[d%4]
            now_y -= dry[d%4]
            d += 1
            now_x += drx[d%4]
            now_y += dry[d%4]
        matrix[now_x][now_y] = n
    print('#{}'.format(test_case))
    for mat in matrix:
        print(*mat)
