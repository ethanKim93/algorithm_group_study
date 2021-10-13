import sys
sys.stdin = open('../ex4/sample_input.txt')


def make_set(x):
    p[x] = x


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def find_set2(x):
    if x == p[x]:
        return x
    else:
        return find_set2(p[x])


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    p = list(range(N+1))

    for i in range(M):
        union(nums[i*2], nums[i*2+1])

    ans = []
    for v in p:
        tmp = find_set(v)
        if tmp not in ans:
            ans.append(tmp)

    print('#{} {}'.format(tc, len(ans)-1))