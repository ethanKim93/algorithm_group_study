import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def binary(A,k,l,r,flag):
    global cnt

    m = (l+r)//2

    if A[m] == k:
        cnt += 1
        return
    if l>=r:
        return
    if flag == 0:
        binary(A,k,l,m-1,1)
        binary(A, k, m+1,r,-1)
    elif flag == 1:
        binary(A, k, m + 1, r, -1)
    elif flag == -1:
        binary(A,k,l,m-1,1)


for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    cnt = 0
    for k in B:
        binary(A,k,0,N-1,0)

    print('#{} {}'.format(tc,cnt))