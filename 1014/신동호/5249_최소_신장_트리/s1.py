import sys
sys.stdin = open('sample_input.txt')

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[] for _ in range(E)]
    p = [i for i in range(V+1)]
    for i in range(E):
        n1, n2, W = map(int, input().split())
        node[i] = W, n1, n2
    node.sort()

    tot = 0
    cnt = 0
    for nd in node:
        if cnt == V:
            break
        W, n1, n2 = nd
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            tot += W
            cnt += 1
    print('#{} {}'.format(tc, tot))

