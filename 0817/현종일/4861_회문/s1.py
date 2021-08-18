import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    field = [list(input()) for _ in range(N)]

    result = ''
    for col in range(N):
        for row in range(N-M+1):
            if field[col][row:row + M] == field[col][row:row + M][::-1]:
                result += ''.join(field[col][row:row + M])

    for col in range(N-M+1):
        for row in range(N):
            match = ''
            for i in range(M):
                match += field[col+i][row]
            if match == match[::-1]:
                result += match

    print('#{} {}'.format(tc, result))

