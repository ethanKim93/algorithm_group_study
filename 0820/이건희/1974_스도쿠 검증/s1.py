import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    maps = [list(map(int,input().split())) for i in range(9)]
    ans = 1
    # Row
    for i in range(9):
        temps = [0] * 10
        for x in range(9):
            if temps[maps[i][x]] == 0:
                temps[maps[i][x]] = 1
            else:
                ans = 0
                break

    # Column
    for i in range(9):
        temps = [0] * 10
        for x in range(9):
            if temps[maps[x][i]] == 0:
                temps[maps[x][i]] = 1
            else:
                ans = 0
                break
    # 3 x 3
    for i in range(3):
        for x in range(3):
            temps = [0] * 10
            for y in range(3):
                for z in range(3):
                    if temps[maps[3*i+y][3*x+z]] == 0:
                        temps[maps[3*i+y][3*x+z]] = 1
                    else:
                        ans = 0
                        break


    print("#{} {}".format(tc, ans))