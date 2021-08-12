import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    c1 = c2 = 0
    for i in range(100):
        c1 += arr[i][i]
        c2 += arr[i][99-i]
    max_sum = c1 if c1 > c2 else c2

    for i in range(100):
        rs = cs = 0
        for j in range(100):
            rs += arr[i][j]
            cs += arr[j][i]
        if max_sum < rs:
            max_sum = rs
        if max_sum < cs:
            max_sum = cs
    print('#{} {}'.format(tc, max_sum))