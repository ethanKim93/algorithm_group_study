import sys
sys.stdin = open('input.txt')

def postorder(t):
    global stack
    if tree[t]:
        postorder(left[t])
        postorder(right[t])
        if type(tree[t]) == int:
            stack += [tree[t]]
        else:
            a = stack.pop()
            b = stack.pop()
            if tree[t] == '+':
                stack += [b + a]
            elif tree[t] == '-':
                stack += [b - a]
            elif tree[t] == '*':
                stack += [b * a]
            elif tree[t] == '/':
                stack += [b / a]



T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    stack = []
    for _ in range(N):
        elements = input().split()
        if len(elements) == 4:
            tree[int(elements[0])] = elements[1]
            left[int(elements[0])] = int(elements[2])
            right[int(elements[0])] = int(elements[3])
        else:
            tree[int(elements[0])] = int(elements[1])
    postorder(1)
    print('#{} {}'.format(tc, int(stack[0])))
