import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    target = 0
    for i in range(100):
        if arr[99][i] == 2:
            target = i
            break

    x = target
    y = 99

    while True:
        if y == 0:
            break

        if x > 0 and arr[y][x-1] == 1:
            while x > 0 and arr[y][x-1] == 1:
                x -= 1
            y -= 1
        elif x < 99 and arr[y][x+1] == 1:
            while x < 99 and arr[y][x+1] == 1:
                x += 1
            y -= 1
        else:
            y -= 1

    print('#{} {}'.format(tc, x))
