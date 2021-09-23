import sys
sys.stdin = open('input.txt')

for tc in range(1, 10+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for x in range(N):
        check = 0
        for y in range(N):
            if check == 0 and MAP[y][x] == 1:
                check = 1
            if check == 1 and MAP[y][x] == 2:
                check = 0
                ans += 1

    print("#{} {}".format(tc, ans))


for tc in range(1, 11):
    length = int(input())
    array = [list(map(int, input().split())) for _ in range(length)]

    EMPTY, N, S = 0, 1, 2
    answer = 0
    for i in range(length - 1):
        for j in range(length):
            if array[i][j] == N:
                if array[i + 1][j] == S:
                    answer += 1
                elif array[i + 1][j] == EMPTY:
                    array[i + 1][j] = array[i][j]

    print('#{} {}'.format(tc, answer))
