import sys
sys.stdin = open('input.txt')


def operation(a):
    if a == '+':
        result = tree[int(node_list[i][2])] + tree[int(node_list[i][3])]
    elif a == '-':
        result = tree[int(node_list[i][2])] - tree[int(node_list[i][3])]
    elif a == '*':
        result = tree[int(node_list[i][2])] * tree[int(node_list[i][3])]
    else:
        result = tree[int(node_list[i][2])] // tree[int(node_list[i][3])]
    return result


for tc in range(1, 11):
    N = int(input())
    node_list = [[]] + [list(input().split()) for _ in range(N)]
    tree = [0] * (N+1)

    for i in range(N, 0, -1):
        if not node_list[i][1].isdecimal():                      # 연산자 인지 판별
            tree[i] = operation(node_list[i][1])
        else:
            tree[i] = int(node_list[i][1])
    print('#{} {}'.format(tc, tree[1]))
