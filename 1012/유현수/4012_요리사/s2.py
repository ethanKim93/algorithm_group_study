import sys
sys.stdin = open('sample_input.txt')


def nC4(n, r, s, k):
    global ans
    if k == r:
        comb2 = list(range(N))
        for i in range(r):
            if comb[i] in comb2:
                comb2.remove(comb[i])
        total = 0
        total2 = 0
        for j in range(0, r):
            for k in range(j+1, r):
                total += synergy[comb[j]][comb[k]] + synergy[comb[k]][comb[j]]
                total2 += synergy[comb2[j]][comb2[k]] + synergy[comb2[k]][comb2[j]]
        minus = abs(total - total2)
        if minus < ans:
            ans = minus
    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            nC4(n, r, i+1, k+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    comb = [0] * (N//2)
    ans = 987654321
    nC4(N, N//2, 0, 0)
    print('#{} {}'.format(tc, ans))
