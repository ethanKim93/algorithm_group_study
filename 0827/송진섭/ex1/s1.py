def pre_order(v):
    if v:
        print(v)
        pre_order(left[v])
        pre_order(right[v])


def in_order(v):
    if v:
        in_order(left[v])
        print(v)
        in_order(right[v])


def post_order(v):
    if v:
        post_order(left[v])
        post_order(right[v])
        print(v)


V = int(input())  # 13
E = V - 1
edge = list(map(int, input().split()))  # 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
left = [0] * (V+1)
right = [0] * (V+1)

for i in range(V-1):
    p, c = edge[i*2], edge[i*2+1]
    if not left[p]:
        left[p] = c
    else:
        right[p] = c
in_order(1)
