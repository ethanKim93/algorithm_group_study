import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    box = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - M + 1):
        for j in range((N-M-1) * (i%2), (N-M) * ((i+1)%2) - 1, 1 - 2*(i%2)):
            for k in range(M):
                box[i][j] - box[i][j]
            print(j, end=' ')
        print('--------')

# 0 N-M 1
# N-M-1 -1 -1
