import sys
sys.stdin = open('sample_input.txt')


def dfs(node):
    global cnt
    cnt += 1
    for n in arr[node]:
        dfs(n)


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))

    arr = [[] for _ in range(E+2)]
    for idx in range(0, len(temp), 2):
        arr[temp[idx]].append(temp[idx+1])

    cnt = 0
    dfs(N)
    print('#{} {}'.format(tc, cnt))
