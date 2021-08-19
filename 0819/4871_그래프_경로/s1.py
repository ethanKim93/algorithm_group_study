import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())  # v = 노드의 갯수, e = 간선의 갯수
    maps = [list(map(int, input().split())) for _ in range(e)] # 간선
    s, g = map(int, input().split())
    stack = []  # 지나온 길
    ans = 0
    already = []  # 연결노드가 더이상 없는 곳까지 도달한 항목들
    while True:
        if s == g:
            ans = 1
            break

        for i in range(e):
            if maps[i][0] == s and maps[i] not in stack and maps[i] not in already:
                stack.append(maps[i])
                s = maps[i][1]
                break
        else:
            if stack:
                end = stack.pop()
                already.append(end)
                s = end[0]

            else:
                break

    print("#{} {}".format(tc, ans))