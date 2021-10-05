# Baby-gin 문제
B = list(map(int, list(input())))

n = len(B)
used = [0] * n
p = [0] * n
flag = 0
def perm(n, k):
    global flag
    if (k==n):
        if (p[0] == p[1] and p[1] == p[2]) or (p[0]+1 == p[1] and p[1]+1 == p[2]):
            if (p[3] == p[4] and p[4] == p[5]) or (p[3] + 1 == p[4] and p[4] + 1 == p[5]):
                flag = 1
    else:
        for i in range(n):
            if not used[i]:
                p[k] = B[i]
                used[i] = True
                perm(n, k + 1)
                used[i] = False

perm(n, 0)
if flag:
    print('Baby-gin')
else:
    print('Not Baby-gin')