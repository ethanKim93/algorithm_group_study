import sys
sys.stdin = open('input.txt')


def pre_order(n):
    if n:
        print(n, end=' ')
        pre_order(left[n])
        pre_order(right[n])


def in_order(n):
    if n:
        in_order(left[n])
        print(n, end=' ')
        in_order(right[n])


def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n, end=' ')


for tc in range(1, 3):
    V = int(input())
    edge = list(map(int, input().split()))
    E = V - 1
    left = [0]*(V+1)
    right = [0]*(V+1)
    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        if not left[p]:
            left[p] = c
        else:
            right[p] = c

    print('#{} '.format(tc))
    pre_order(1)
    print()
    in_order(1)
    print()
    post_order(1)
    print()