# 에러 1개

import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(T):
    N = list(map(int, input().split()))
    a = []
    b = []
    result = '0'
    for i in range(0, len(N), 2):
        a.append(N[i])
        b.append(N[i + 1])
        if result != '0':
            break
        elif len(a) >= 3:
            for j in range(len(a) - 2):
                a.sort()
                b.sort()
                if result != '0':
                    break
                elif result == '0':
                    if a[j] + 2 == a[j + 1] + 1 == a[j + 2] or a[j] == a[j + 1] == a[j + 2]:
                        result = '1'
                    elif b[j] + 2 == b[j + 1] + 1 == b[j + 2] or b[j] == b[j + 1] == b[j + 2]:
                        result = '2'
    print('#{} {}'.format(tc + 1, result))
