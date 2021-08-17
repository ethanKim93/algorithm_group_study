import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    bar = input()

    bar_cnt = 0
    total = 0
    idx = 0
    while True:
        if idx >= len(bar):
            break

        if bar[idx] == '(':
            bar_cnt += 1
        else:
            if bar[idx-1] == '(':
                bar_cnt -= 1
                total += bar_cnt
            else:
                bar_cnt -= 1
                total += 1

        idx += 1
    print('#{} {}'.format(tc, total))

