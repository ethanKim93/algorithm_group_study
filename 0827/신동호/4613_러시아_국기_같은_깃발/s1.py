import sys
sys.stdin = open('sample_input.txt')

def color(mat):
    global result
    for i in range(1, N-1):
        for j in range(i+1, N):
            subsum = 0
            for x in range(0, i):
                subsum += M - mat[x][0]
            for y in range(i, j):
                subsum += M - mat[y][1]
            for z in range(j, N):
                subsum += M - mat[z][2]
            if subsum < result:
                result = subsum




T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [[0]*3 for _ in range(N)]
    result = N * M
    for n in range(N):
        inf = list(input())
        for f in inf:
            if f == 'W':
                matrix[n][0] += 1
            elif f == 'B':
                matrix[n][1] += 1
            elif f == 'R':
                matrix[n][2] += 1
    color(matrix)
    print('#{} {}'.format(tc, result))