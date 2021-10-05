# RunTime Error 코드
# pop 은 느리다!!!

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    container, truck = map(int, input().split())
    w = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    ans = 0

    if w[0] > c[-1]:
        print('#{} {}'.format(tc, ans))

    else:
        while len(c) != 0 and len(w) != 0:
            while True:
                if w[-1] <= c[-1]:
                    ans += w.pop(-1)
                    break
                else:
                    w.pop(-1)
            c.pop(-1)

        print('#{} {}'.format(tc, ans))
