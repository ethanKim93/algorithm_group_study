import sys
sys.stdin = open('input.txt')


def post_order(v):
    if v:
        post_order(left[v])
        post_order(right[v])
        print(v)


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

post_order(1)