import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    numeber = [list(map(int, input().split())) for _ in range(N)]
    print(numeber)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    sums1 = 0
    sums2 = 0


    for x in range(len(numeber)):
        for y in range(len(numeber[x])):
            for i in range(4):
                testX = x + dx[i]
                testY = y + dy[i]
                if 0 <= testX < len(numeber) and 0 <= testY < len(numeber[x]):
                    sums1 = abs(numeber[testX][testY] - numeber[x][y])
                    sums2 += sums1
    print(sums2)




