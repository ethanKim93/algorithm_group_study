import sys
sys.stdin = open('sample_input.txt')


def nC4(n, s, k):
    global ans
    if k == 4:
        min_diff = 987654321
        for i1 in range(4):
            for i2 in range(4):
                if i2 != i1:
                    for i3 in range(4):
                        if i3 != i1 and i3 != i2:
                            for i4 in range(4):
                                if i4 != i3 and i4 != i2 and i4 != i1:
                                    a1, a2, b1, b2 = comb[i1], comb[i2], comb[i3], comb[i4]
                                    # print(a1, a2, b1, b2)
                                    A = synergy[a1][a2] + synergy[a2][a1]
                                    B = synergy[b1][b2] + synergy[b2][b1]
                                    if min_diff > abs(A-B):
                                        min_diff = abs(A-B)
        if ans > min_diff:
            ans = min_diff
    else:
        for i in range(s, n+k-3):
            comb[k] = i
            nC4(n, i+1, k+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    comb = [0] * 4
    ans = 987654321
    nC4(N, 0, 0)
    print('#{} {}'.format(tc, ans))

