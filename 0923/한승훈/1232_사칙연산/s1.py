import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    nodes = [0] * (N+1)
    f = ['+', '-', '/', '*']
    line = [[] for _ in range(N+1)]
    for _ in range(N):
        lst = list(input().split())
        nodes[int(lst[0])] = lst[1]
        if len(lst) == 4:
            line[int(lst[0])] += [int(lst[2]), int(lst[3])]

    for i in range(N, 0, -1):
        if nodes[i] in f:
            l = int(nodes[line[i][0]])
            r = int(nodes[line[i][1]])
            if nodes[i] == '+':
                nodes[i] = l + r
            elif nodes[i] == '-':
                nodes[i] = l - r
            elif nodes[i] == '/':
                nodes[i] = l / r
            else:
                nodes[i] = l * r

    print('#{} {}'.format(tc, int(nodes[1])))