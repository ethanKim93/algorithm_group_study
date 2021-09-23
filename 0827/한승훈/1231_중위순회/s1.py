import sys
sys.stdin = open('input.txt')


def inorder(n):
    if n <= N:
        inorder(n*2)  # 왼쪽
        print(tree[n], end='')
        inorder(n*2+1)  # 오른쪽


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    lst = [input().split() for _ in range(N)]
    for i in range(N):
        tree[i+1] = lst[i][1]
    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()