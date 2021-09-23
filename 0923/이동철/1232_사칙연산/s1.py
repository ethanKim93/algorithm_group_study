import sys
sys.stdin = open('input.txt')


def post_order(n):
    global stack
    if tree[n]:
        post_order(left[n])
        post_order(right[n])
        if type(tree[n]) == int:
            stack += [tree[n]]
        else:
            a = stack.pop()
            b = stack.pop()
            if tree[n] == '+':
                stack += [b + a]
            elif tree[n] == '-':
                stack += [b - a]
            elif tree[n] == '*':
                stack += [b * a]
            elif tree[n] == '/':
                stack += [b / a]


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(N):
        temp = input().split()
        if len(temp) == 4:
            tree[int(temp[0])] = temp[1]
            left[int(temp[0])] = int(temp[2])
            right[int(temp[0])] = int(temp[3])
        else:
            tree[int(temp[0])] = int(temp[1])

    stack = []
    post_order(1)
    print('#{} {}'.format(tc, int(stack[0])))