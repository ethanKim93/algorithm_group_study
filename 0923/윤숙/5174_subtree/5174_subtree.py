import sys
sys.stdin=open('input.txt')


def pre_order(n):
    global cnt
    if n:
        cnt+=1
        pre_order(left[n])
        pre_order(right[n])


T=int(input())
for tc in range(1,T+1):

    E,N=map(int,input().split())
    V=E+1
    left=[0]*(V+1)
    right=[0]*(V+1)
    tree=list(map(int,input().split()))
    # 0 1 2 3 4 5 6 7 8 9
    # 2 1 2 5 1 6 5 3 6 4
    for i in range(0, len(tree), 2):
        parent, child = tree[i], tree[i + 1]
        if not left[parent]:
            left[parent] = child
        else:
            right[parent] = child

    cnt=0
    pre_order(N)
    print('#{} {}'.format(tc,cnt))

