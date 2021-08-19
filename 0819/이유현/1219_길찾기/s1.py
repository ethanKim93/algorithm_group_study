import sys
sys.stdin = open('input.txt')


def dfs(start, end):
    route = []
    route.append(start)

    while route:
        now = route.pop()
        visit[now] = 1

        for i in range(1, 101):
            if d[now][i] == 1 and visit[i] == 0:
                route.append(i)
    if visit[end] == 1:
        return 1
    else:
        return 0


for tc in range(1, 11):
    N, E = map(int, input().split())
    temp = list(map(int, input().split()))

    d = [[0]*101 for _ in range(101)]
    visit = [0 for _ in range(101)]
    for i in range(0, len(temp), 2):
        d[temp[i]][temp[i+1]] = 1

    S, G = 0, 99
    print('#{} {}'.format(tc, dfs(0, 99)))

