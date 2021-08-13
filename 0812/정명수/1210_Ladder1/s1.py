import sys
sys.stdin = open('input.txt')

for test_case in range(1,11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    for k in range(100):
        ladder[k].insert(0,0)
        ladder[k].append(0)
    for i in range(len(ladder)):
        if ladder[99][i] == 2:
            now_col = i
            break
    now_height = 99
    for _ in range(100):
        if ladder[now_height][now_col-1] == 1:
            now_col -= 1
            while ladder[now_height-1][now_col] != 1:
                now_col -= 1
            now_height -= 1
            if now_height == 0:
                print('#{} {}'.format(test_case, now_col - 1))
            continue

        if ladder[now_height][now_col+1] == 1:
            now_col += 1
            while ladder[now_height-1][now_col] != 1:
                now_col += 1
            now_height -= 1
            continue
            if now_height == 0:
                print('#{} {}'.format(test_case, now_col - 1))
        now_height -= 1
        if now_height == 0:
            print('#{} {}'.format(test_case, now_col-1))





