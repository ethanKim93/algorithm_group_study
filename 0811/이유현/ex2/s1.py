import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    total = []

    for i in range(1 << n):
        p = []
        for j in range(n):
            if i & (1<<j):
                p += [arr[j]]
        total.append(p)

    for p_list in total[1:]:
        if sum(p_list) == 0:
            result = 1
            break
    else:
        result = 0
    print('#{} {}'.format(tc, result))
