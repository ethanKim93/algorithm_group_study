import sys
sys.stdin = open('input.txt')


def in_order(v):
    if v:
        in_order(left[v])
        print(v)
        in_order(right[v])


V = int(input())
edge = list(map(int, input().split()))
E = V - 1

left = [0]*(V+1)
right = [0]*(V+1)

for i in range(0, E*2, 2):
    x, y = edge[i], edge[i+1]
    if not left[x]:
        left[x] = y
    else:
        right[x] = y

in_order(1)