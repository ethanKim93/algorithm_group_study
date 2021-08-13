import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    field = [[0] * N for _ in range(N)]

    for i in range(N):
        arr = list(map(int,input().split()))
        for j in range(N):
            field[i][j] = arr[j]


    maxkill = -1
    for k in range(N-M+1):
        for l in range(N-M+1):
            flysum = 0
            for m in range(M):
                for n in range(M):
                    flysum += field[k+m][l+n]
            if flysum > maxkill:
                maxkill = flysum

    print('#{} {}'.format(tc,maxkill))