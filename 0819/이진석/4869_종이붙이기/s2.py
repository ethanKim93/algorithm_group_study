import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    p = 1
    n = N // 10
    for i in range(1, n + 1):   # 1, 3, 5, 11, 21, 43, 85, ...
        if i % 2:
            p = (p * 2) - 1
        else:
            p = (p * 2) + 1
    print('#{} {}'.format(tc, p))
