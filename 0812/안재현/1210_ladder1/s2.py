import sys

sys.stdin = open('input.txt')

for T in range(10):
    tc = int(input())

    input_map = [list(map(int, input().split())) for _ in range(100)]
    r = 99
    s = -1
    for i in range(100):
        if input_map[99][i] == 2:
            s = i

    while True:
        input_map[r][s] = 0
        if s - 1 >= 0 and input_map[r][s - 1]:
            s -= 1
            continue
        if s + 1 < 100 and input_map[r][s + 1]:
            s += 1
            continue
        if r - 1 >= 0:
            r -= 1
            continue
        else:
            break
    print('#{} {}'.format(tc, s))