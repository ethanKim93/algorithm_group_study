import sys
sys.stdin = open('input.txt')



for _ in range(1, 11):
    tc = int(input())
    ladders = list(list(map(int, input().split())) for _ in range(100))


    s = ladders[99].index(2)
    x, y = 99, s
    finish = [[0] * 100 for _ in range(100)]
    while x != 0:
        finish[x][y] = 1
        if y - 1 >= 0 and ladders[x][y - 1] and finish[x][y - 1] == 0:
            y -= 1
            continue
        elif y + 1 < 100 and ladders[x][y + 1] and finish[x][y + 1] == 0:
            y += 1
            continue
        else:
            x -= 1

    answer = y

    print('#{} {}'.format(tc, answer))

