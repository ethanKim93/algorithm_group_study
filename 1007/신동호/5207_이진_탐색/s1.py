import sys
sys.stdin = open('sample_input.txt')

def check(b):
    global cnt, A
    l = 0
    r = N-1
    flag = 0
    while l <= r:
        m = (l+r)//2
        if A[m] == b:
            cnt += 1
            # print(A[m], end=' ')
            return
        elif A[m] > b:
            if flag == 'L':
                return
            r = m-1
            flag = 'L'
            # check(b, l, m-1, 'L')
        else:
            if flag == 'R':
                return
            l = m+1
            flag = 'R'
            # check(b, m+1, r, 'R')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int ,input().split())))
    B = list(map(int ,input().split()))
    cnt = 0
    for b in B:
        check(b)
    # print()
    print('#{} {}'.format(tc, cnt))