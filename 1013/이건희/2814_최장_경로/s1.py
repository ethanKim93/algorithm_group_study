import sys
sys.stdin = open("input.txt")


def dfs(start, cnt, visited):
    global ans
    if cnt > ans:
        ans = cnt

    for i in maps[start]:
        if i not in visited:
            dfs(i, cnt + 1, visited + [i])

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    maps = [[] for _ in range(n + 1)]
    ans = 1
    for i in range(m):
        a, b = map(int, input().split())
        maps[a].append(b)
        maps[b].append(a)

    for i in range(1, n):
        dfs(i, 1, [i])

    print("#{} {}".format(tc, ans))

# Pass