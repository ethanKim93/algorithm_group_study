import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    mat_90 = [[0]*N for _ in range(N)]
    mat_180 = [[0]*N for _ in range(N)]
    mat_270 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mat_90[i][j] = matrix[N-1-j][i]
            mat_180[i][j] = matrix[N-1-i][N-1-j]
            mat_270[i][j] = matrix[j][N-1-i]
    print('#{}'.format(tc))
    for x in range(N):
        print(''.join(map(str, mat_90[x])), end=' ')
        print(''.join(map(str, mat_180[x])), end=' ')
        print(''.join(map(str, mat_270[x])))