import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for x in range(M):
                for y in range(M):
                    kill += matrix[i+x][j+y]

            if max_kill < kill:
                max_kill = kill
    print('#{} {}'.format(tc, max_kill))
