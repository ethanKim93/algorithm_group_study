import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    box = [list(map(int, input().split())) for _ in range(N)]
    max_sub = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sub = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                   sub += box[x][y]
            if max_sub < sub:
                max_sub = sub
    print('#{} {}'.format(tc,max_sub))


