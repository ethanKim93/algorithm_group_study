import sys
sys.stdin = open('input.txt')

def postorder(n):
    if n:
        postorder(left[n])
        postorder(right[n])
        if tree[n] == '+':
            tree[n] = tree[left[n]] + tree[right[n]]
        elif tree[n] == '-':
            tree[n] = tree[left[n]] - tree[right[n]]
        elif tree[n] == '*':
            tree[n] = tree[left[n]] * tree[right[n]]
        elif tree[n] == '/':
            tree[n] = tree[left[n]] / tree[right[n]]


T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    for _ in range(N):
        edge = input().split()
        if len(edge) == 2:
            tree[int(edge[0])] = int(edge[1])
        else:
            tree[int(edge[0])] = edge[1]
            left[int(edge[0])] = int(edge[2])
            right[int(edge[0])] = int(edge[3])
    postorder(1)
    print('#{} {}'.format(tc, int(tree[1])))