import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]


    kill_flies = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0

            for a in range(M):
                for b in range(M):
                    kill += flies[i+a][j+b]

            kill_flies.append(kill)


    big = 0
    for fly in kill_flies:
        if fly > big:
            big = fly

    print('#{} {}'.format(tc, big))

