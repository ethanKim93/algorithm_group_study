import sys

sys.stdin = open('sample_input.txt')

T = int(input())


def sub_tree(n):
    global cnt
    if n == 0:
        return
    cnt += 1
    sub_tree(left[n])
    sub_tree(right[n])


for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    left = right = [0] * (E + 2)

    for i in range(0, len(tree), 2):
        p, c = tree[i], tree[i + 1]  # p - 부모  c - 자식
        if left[p]:
            right[p] = c
        else:
            left[p] = c

    cnt = 0
    sub_tree(N)
    print('# {} {}'.format(tc, cnt))