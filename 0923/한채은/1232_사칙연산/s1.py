import sys
sys.stdin = open('input.txt')


def change(op):
    if op == '+':
        ans = tree[int(info[i][2])] + tree[int(info[i][3])]
    if op == '-':
        ans = tree[int(info[i][2])] - tree[int(info[i][3])]
    if op == '*':
        ans = tree[int(info[i][2])] * tree[int(info[i][3])]
    if op == '/':
        ans = tree[int(info[i][2])] // tree[int(info[i][3])]
    return ans


cal = ['+', '-', '*', '/']

for tc in range(1, 11):
    N = int(input())
    info = [0] + [list(input().split()) for _ in range(N)]
    tree = [0] * (N+1)


    # 1까지만 필요하니까 범위는 0까지
    for i in range(N, 0, -1):
        if info[i][1] in cal:
            tree[i] = change(info[i][1])
        else:
            tree[i] = int(info[i][1])

    print('#{} {}'.format(tc, tree[1]))
