import sys
sys.stdin = open('input.txt')

def postorder(i):
    if type(nodes[i]) == str:
        l = postorder(left[i])
        r = postorder(right[i])
        if nodes[i] == '+':
            nodes[i] = l + r
        if nodes[i] == '-':
            nodes[i] = l - r
        if nodes[i] == '*':
            nodes[i] = l * r
        if nodes[i] == '/':
            nodes[i] = l / r
    return nodes[i]


for tc in range(1, 11):
    N = int(input())
    nodes = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)
    for _ in range(N):
        n, *arg = input().split()
        try:
            nodes[int(n)] = arg[0]
            left[int(n)] = int(arg[1])
            right[int(n)] = int(arg[2])
        except:
            nodes[int(n)] = int(arg[0])
            left[int(n)] = int(n)*2
            right[int(n)] = int(n)*2+1

    postorder(1)
    print('#{} {}'.format(tc, int(nodes[1])))

