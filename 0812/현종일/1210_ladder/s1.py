import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    col = 99
    row = -1

    for i in range(len(ladder[99])):
        if ladder[99][i] == 2:
            row = i

    while True:
        if col == 0:
            break

        if row < 99 and ladder[col][row + 1]:
            while ladder[col][row + 1] if row < 99 else False:
                row += 1
            col -= 1
        elif row > 0 and ladder[col][row - 1]:
            while ladder[col][row - 1] if row > 0 else False:
                row -= 1
            col -= 1
        else:
            col -= 1

    print('#{} {}'.format(tc, row))