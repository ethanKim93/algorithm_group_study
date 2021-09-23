import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    num = [0]*(N+1)
    for _ in range(M):
        l1,l2 = map(int,input().split())
        num[l1] = l2
    for i in range(N,0,-1):
        num[i//2] += num[i]
    print('#{} {}'.format(tc,num[L]))