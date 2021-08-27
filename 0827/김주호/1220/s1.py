import sys
sys.stdin = open("input.txt")

for case in range(10):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if table[row][col] == 2:
                step = 1
                while -1 < row - step:
                    if table[row - step][col] != 0:
                        table[row][col] = 0
                        table[row - step + 1][col] = 2
                        break
                    step += 1
                else:
                    table[row][col] = 0

    result = 0
    for r in range(N - 1):
        for c in range(N):
            if table[r][c] == 1 and table[r+1][c] == 2:
                result += 1

    print("#{} {}".format(case + 1, result))
