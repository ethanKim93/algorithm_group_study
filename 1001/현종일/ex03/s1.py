N = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]


def nCr(r, s, k):
    if k == r:
        if sum(comb) == 0:
            print(*comb)
    else:
        for i in range(s, 10-r+k+1):
            comb[k] = N[i]
            nCr(r, i+1, k+1)


for j in range(1, len(N)):
    comb = [0] * j
    nCr(j, 0, 0)
