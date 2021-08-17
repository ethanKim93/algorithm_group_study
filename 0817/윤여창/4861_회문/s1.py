import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    border = [list(input()) for _ in range(N)]

    for row in range(N):
        for col in range(N-M+1):
            if border[row][col:col+M] == border[row][col:col+M][::-1]:
                print('#{} {}'.format(tc, ''.join(border[row][col:col+M])))
                break
    else:
        word = ''
        for col in range(N):
            for row in range(N - M + 1):
                for k in range(M):
                    word += border[row + k][col]
                if word == word[::-1]:
                    print('#{} {}'.format(tc, word))
                    break
                else:
                    word = '' #초기화