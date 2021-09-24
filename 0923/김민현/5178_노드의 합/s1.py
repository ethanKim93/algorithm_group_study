import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    tree = [0]*(N+1)
    for i in range(M):
        idx,val = map(int,input().split())
        tree[idx] = val

    for j in range(N,-1,-1):
        if not tree[j]:
            if (j*2)+1 <= N:
                tree[j] = tree[j*2]+tree[(j*2)+1]
            elif (j*2) == N:
                tree[j] = tree[j * 2]
            else:
                pass
    print('#{} {}'.format(tc, tree[L]))


