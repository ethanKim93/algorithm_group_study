import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def inorder(node, N):
    global cnt
    if node <= N:
        inorder(2*node, N)
        cnt += 1
        tree[node] = cnt
        inorder(2*node + 1, N)

for tc in range(1, 1 + T):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 0

    inorder(1, N)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))