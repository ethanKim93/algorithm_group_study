import sys

sys.stdin = open('input.txt')


def pre_order(v):
    if v:
        print(v)
        pre_order(left[v])
        pre_order(right[v])


V = int(input())
E = V - 1
edge = list(map(int, input().split()))

left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(0, E*2, 2):
    x, y = edge[i], edge[i+1]
    if not left[x]:
        left[x] = y
    else:
        right[x] = y

pre_order(1)