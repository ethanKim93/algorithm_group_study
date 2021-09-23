import sys
sys.stdin = open('sample_input.txt')


def tree(i):
    global cnt
    if i <= N:
        # 왼쪽
        tree(i*2)
        base_tree[i] = cnt
        cnt += 1
        # 오른쪽
        tree(i*2+1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    base_tree = [0 for _ in range(N+1)]

    cnt = 1
    tree(1)
    root = base_tree[1]
    node = base_tree[N//2]
    print('#{} {} {}'.format(tc, root, node))
