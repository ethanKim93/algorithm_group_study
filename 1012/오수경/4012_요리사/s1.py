# testcase 9 10 왜 안나오지...
# 수정필요

import sys
sys.stdin = open('sample_input.txt')


def make_synergy(lst):
    synergy = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            synergy += (S[lst[i]-1][lst[j]-1] + S[lst[j]-1][lst[i]-1])

    return synergy


def combination(n):
    foods = list(range(1, N+1))
    picked = [0]*N
    return_pick = []

    def generate(tmp, picked):
        global N, ans
        if len(tmp) == N/2:
            x = sorted(tmp)[:]
            if x not in return_pick:
                return_pick.append(x)
                b = list(set(foods)-set(x))
                gap = abs(make_synergy(x) - make_synergy(b))
                if gap < ans:
                    ans = gap
                    return
            return

        else:
            for i in range(N):
                if picked[i] != 1:
                    tmp.append(foods[i])
                    picked[i] = 1

                    generate(tmp, picked)
                    picked[i] = 0
                    tmp.pop()

    generate([], picked)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    ans = 999999

    combination(N)
    print('#{} {}'.format(tc, ans))
