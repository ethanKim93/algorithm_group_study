import sys
sys.stdin = open('sample_input.txt')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    vote = list(map(int, input().split()))
    p = [i for i in range(N+1)]

    for i in range(M):
        union(vote[i*2], vote[i*2+1])

    repr = []
    for i in range(N+1):
        if find_set(i) not in repr:
            repr.append(find_set(i))

    print('#{} {}'.format(tc, len(repr)-1))
