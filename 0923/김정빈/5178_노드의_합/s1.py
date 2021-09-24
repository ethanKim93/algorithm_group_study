import sys
sys.stdin = open("input.txt")
#5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for i in range(M):
        n, v = map(int, input().split())
        tree[n] = v
    print(tree)
    for j in range(N,0,-1):
        tree[j//2] += tree[j]
    print(tree)
    print('#{} {}'.format(tc, tree[L]))