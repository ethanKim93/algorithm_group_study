import sys
sys.stdin = open('input.txt')

def post(V):
    if V >= N:
        return
    if tree[V][2]:
        post(tree[V][2])
    if tree[V][3]:
        post(tree[V][3])

    if tree[V][1] == '+':
        tree[V][1] = tree[tree[V][2]][1] + tree[tree[V][3]][1]
    elif tree[V][1] == '-':
        tree[V][1] = tree[tree[V][2]][1] - tree[tree[V][3]][1]
    elif tree[V][1] == '*':
        tree[V][1] = tree[tree[V][2]][1] * tree[tree[V][3]][1]
    elif tree[V][1] == '/':
        tree[V][1] = tree[tree[V][2]][1] / tree[tree[V][3]][1]


for tc in range(1,11):
    N = int(input())
    tree = [[0]*4 for _ in range(N+1)]

    for n in range(N):
        li = list(input().split())
        if li[1].isdigit():
            tree[int(li[0])][1] = int(li[1])
        else:
            tree[int(li[0])][1] = li[1]
            tree[int(li[0])][2] = int(li[2])
            tree[int(li[0])][3] = int(li[3])

    post(1)
    print('#{} {}'.format(tc, int(tree[1][1])))
