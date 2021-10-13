# pass 코드!

import sys
sys.stdin = open('sample_input.txt')


def make_synergy(lst):
    synergy = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            synergy += (S[lst[i]-1][lst[j]-1] + S[lst[j]-1][lst[i]-1])

    return synergy


def combination(lst, n):
    ret = []
    if n > len(lst):
        return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in combination(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    ans = 999999
    foods = list(range(1, N + 1))
    lst = combination(foods, N//2)
    for l in lst:
        b = list(set(foods) - set(l))
        gap = abs(make_synergy(l) - make_synergy(b))
        if gap < ans:
            ans = gap

    print('#{} {}'.format(tc, ans))
