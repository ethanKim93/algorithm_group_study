import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [list(input()) for _ in range(N)]

    result = []
    for r in range(N):
        for c in range(N - M + 1):
            if table[r][c:c+M] == table[r][c:c+M][::-1]:
                result.append(''.join(table[r][c:c+M]))

    for r in range(N - M + 1):
        for c in range(N):
            c_list = []
            for i in range(M):
                c_list.append(table[r+i][c])
            if c_list == c_list[::-1]:
                result.append(''.join(c_list))

    print('#{} {}'.format(tc, *result))
