import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)]

    result = 0
    for i in range(N//2+1):
        for j in range(N//2 - i, N//2 + i + 1):
            result += field[i][j]
            if not i == N//2:
                result += field[N-1-i][j]

    print('#{} {}'.format(tc, result))

