import sys

sys.stdin = open('input (12).txt')


def check_road():
    now = 0  # 시작점   A
    goal = 99  # 도착점  B
    visited = [0] * 100  # 방문기록
    stack = []  # 스택
    stack.append(now)
    while True:
        for i in range(100):
             if arr[now][i] and visited[i] < 2:
                now = i
                visited[now] += 1
                stack.append(now)
                if now == goal:
                    return 1
                break

        else :
            if stack:
                now = stack.pop()
            else:
                break


    return 0

for _ in range(1, 11):
    tc, N = map(int, input().split())
    arr = [[0]*100 for _ in range(100)]
    string = list(map(int, input().split()))
    for i in range(0, len(string), 2):
        n = string[i]
        m = string[i + 1]
        arr[n][m] = 1
    result = check_road()
    print('#{} {}'.format(tc, result))