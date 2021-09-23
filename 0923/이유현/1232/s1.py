import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    num_tree = [0] * (N+1)

    for _ in range(N):
        temp = list(input().split())
        if len(temp) > 2:
            tree[int(temp[0])].append(temp[1])
            tree[int(temp[0])] += list(map(int, temp[2:]))

        else:
            num_tree[int(temp[0])] = int(temp[1])

    for t in range(N, 0, -1):
        if tree[t]:
            opt = tree[t].pop(0)
            idx1 = tree[t].pop(0)
            idx2 = tree[t].pop(0)
            if opt == '+':
                num_tree[t] = num_tree[idx1] + num_tree[idx2]
            elif opt == '-':
                num_tree[t] = num_tree[idx1] - num_tree[idx2]
            elif opt == '*':
                num_tree[t] = num_tree[idx1] * num_tree[idx2]
            elif opt == '/':
                num_tree[t] = num_tree[idx1] // num_tree[idx2]

    print('#{} {}'.format(tc, num_tree[1]))