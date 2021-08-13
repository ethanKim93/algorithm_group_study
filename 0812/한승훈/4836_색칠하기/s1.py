import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0]*10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        ij = list(map(int, input().split()))
        x_start, y_start = ij[0], ij[1]
        dx, dy = ij[2] - ij[0], ij[3] - ij[1]
        color = ij[4]
        for i in range(dx+1):
            for j in range(dy+1):
                matrix[x_start+i][y_start+j] += color

    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(tc, cnt))

