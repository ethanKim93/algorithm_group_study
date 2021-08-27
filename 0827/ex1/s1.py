import sys

sys.stdin = open('input.txt')


def pre_order(v):
    if v:
        print(v)
        pre_order(left[v])
        pre_order(right[v])


T = int(input())
N = list(map(int, input().split()))
h = T - 1

left = [0] * (T + 1)
right = [0] * (T + 1)

for i in range(h):
    p, c = N[2 * i], N[2 * i + 1]
    if not left[p]:
        left[p] = c
    else:
        right[p] = c

pre_order(1)
