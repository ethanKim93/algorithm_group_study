import sys
sys.stdin=open('input.txt')

for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    totals = []

    for i in range(100):
        r_total = 0
        for j in range(100):
            r_total += arr[i][j]
        totals += [r_total]

    for j in range(100):
        c_total = 0
        for i in range(100):
            c_total += arr[i][j]
        totals += [c_total]

    d1 = 0
    for i in range(100):
        d1 += arr[i][i]
    totals += [d1]

    d2 = 0
    for i in range(100):
        d2 += arr[i][99-i]
    totals += [d2]

    result = totals[0]
    for i in range(202):
        if result < totals[i]:
            result = totals[i]

    print('#{} {}'.format(T, result))