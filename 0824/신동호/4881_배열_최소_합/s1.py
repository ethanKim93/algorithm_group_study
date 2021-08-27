import sys
sys.stdin = open('sample_input.txt')

def check(row = 0, subsum = 0):
    global tot
    if tot <= subsum:
        return
    if row == N:
        if tot > subsum:
            tot = subsum
        return
    for j in range(N):
        if not used[j]:
            used[j] = 1
            check(row + 1, subsum + mat[row][j])
            used[j] = 0


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    tot = 10000
    check()
    print('#{} {}'.format(tc, tot))


