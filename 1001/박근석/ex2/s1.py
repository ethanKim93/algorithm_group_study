
p = []
arr = [1,2,1,1,1,1]
used = [False, False, False, False, False, False]

def perm(n, k):
    if k == n:
        print(p)
    else:
        for i in range(0, n-1):
            if not used[i]:
                p[k] =
                p[k], p[i] = p[i], p[k]
                perm(n, k+1)
                p[k], p[i] = p[i], p[k]

perm(6,1)