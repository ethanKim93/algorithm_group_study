import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    N = int(input())
    tree = [0]*(N+1)
    orders = [list(input().split()) for _ in range(N)]
    for order in orders[::-1]:
        try:
            int(order[1])
            tree[int(order[0])] = int(order[1])
        except:
            if order[1] == '+':
                tree[int(order[0])] = tree[int(order[2])] + tree[int(order[3])]
            elif order[1] == '-':
                tree[int(order[0])] = tree[int(order[2])] - tree[int(order[3])]
            elif order[1] == '*':
                tree[int(order[0])] = tree[int(order[2])] * tree[int(order[3])]
            elif order[1] == '/':
                tree[int(order[0])] = tree[int(order[2])] / tree[int(order[3])]
    print('#{} {}'.format(tc,int(tree[1])))