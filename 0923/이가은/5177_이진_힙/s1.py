import sys
sys.stdin = open('sample_input.txt')

def heap(cnt):
    node = cnt //2
    if tree[node] > tree[cnt]:
        tree[node], tree[cnt] = tree[cnt], tree[node]
        heap(node)


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    tree = [0]
    cnt = 1
    for n in map(int, input().split()):
        tree.append(n)
        heap(cnt)
        cnt += 1

    result = 0
    while N:
        N //= 2
        result += tree[N]

    print('#{} {}'.format(tc, result))
