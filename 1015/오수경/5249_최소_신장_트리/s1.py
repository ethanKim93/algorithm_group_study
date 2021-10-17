import sys
sys.stdin = open('sample_input.txt')

def Find_Set(x):
    if node[x] == x:
        return x
    else:
        return Find_Set(node[x])

def Union(x, y):
    node[Find_Set(y)] = Find_Set(x)

def is_cycle(x,y):
    if Find_Set(x) == Find_Set(y):
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = list(range(V+1))

    visited = [0]*(V+1)
    link = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        link.append([w, n1, n2])

    link.sort()
    min_weight = 0
    for w, n1, n2 in link:
        if is_cycle(n1, n2):
            continue
        else:
            min_weight += w
            Union(n1, n2)

    print('#{} {}'.format(tc, min_weight))
