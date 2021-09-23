import sys
sys.stdin = open('sample_input.txt')


def min_heap(n):
    if n > 0:
        if tree[n//2] > tree[n]:
            tree[n], tree[n // 2] = tree[n // 2], tree[n]
            min_heap(n // 2)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nodes = list(map(int, input().split()))

    tree = [0] * (N+1)
    for i in range(0, N):
        tree[i+1] = nodes[i]
    for num in range(1, len(tree)):
        min_heap(num)

    total = 0
    
