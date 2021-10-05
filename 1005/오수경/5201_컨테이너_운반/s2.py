# pass 코드

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    container, truck = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    c = sorted(list(map(int, input().split())), reverse=True)
    ans = 0

    if w[0] < c[-1]:
        print('#{} {}'.format(tc, ans))

    else:
        i = 0
        x = 0
        while i < truck:
            for j in range(x, container):
                if w[j] <= c[i]:
                    ans += w[j]
                    x += 1
                    break
                else:
                    x += 1
                    continue
            i += 1
        print('#{} {}'.format(tc, ans))
