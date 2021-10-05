import sys
sys.stdin = open('input.txt')


def check(s):
    triplet = 0
    run = 0
    for i in range(2):
        if s[i*3] == s[1+i*3] == s[2+i*3]:
            triplet += 1
        elif s[i*3]+2 == s[1+i*3]+1 == s[2+i*3]:
            run += 1
    if triplet + run == 2:
        return 1
    return 0


def perm(n, k):
    global ans
    if ans:
        return
    if k == n:
        if check(p):
            ans = True
    else:
        for i in range(n-1):
            p[k], p[i] = p[i], p[k]
            perm(n, k+1)
            p[k], p[i] = p[i], p[k]


T = int(input())
for tc in range(1, T+1):
    p = list(map(int, list(input())))
    ans = False
    perm(6, 0)
    print('#{} {}'.format(tc, ans))
