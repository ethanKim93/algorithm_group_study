import sys
sys.stdin=open('input.txt')
T= int(input())

for tc in range(1,T+1):
    # N : 노드의 개수
    # M : 리프노드의 갯수
    # L : 값을 출력할 노드 번호

    N,M,L=map(int,input().split())
    tree = [0] * (N + 1)
    for i in range(M):
        idx,num=map(int,input().split())
        tree[idx]=num

    for i in range(N//2,0,-1):
        if tree[i]==0:
            if (i*2 <=N) and (i*2+1<=N):
                tree[i]=tree[i*2]+tree[i*2+1]
            elif i*2+1>N:
                tree[i]=tree[i*2]

    print('#{} {}'.format(tc,tree[L]))