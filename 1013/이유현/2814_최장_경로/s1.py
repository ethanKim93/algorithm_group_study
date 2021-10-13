import sys
sys.stdin = open('sample_input.txt')


def dfs(idx, cnt):
    global ans
    visit[idx] = 0
    cnt += 1
    if ans < cnt:
        ans = cnt
    for i in arr[idx]:
        if visit[i]:
            dfs(i, cnt)
    visit[idx] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visit = [1 for _ in range(N+1)]
    temp = [list(map(int, input().split())) for _ in range(M)]
    arr = [[] for _ in range(N+1)]
    ans = 0
    for a, b in temp:
        arr[a].append(b)
        arr[b].append(a)

    for i in range(N):
        dfs(i, 0)
    print('#{} {}'.format(tc, ans))