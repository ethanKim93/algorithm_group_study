import sys
sys.stdin = open('sample_input.txt')

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

dessert = [False] * 101 # 지나간 디저트 카페 표시
# d는 방향, l은 진행칸수
def dfs(x, y, l, d):

    global answer, dessert

    if d == 3 and x == sx and y == sy: # 출발점에 도착한경우
        answer = max(answer, l)
        return
    elif x < 0 or x >= N or y < 0 or y >= N:
        return
    elif dessert[arr[x][y]]:        # 이미 방문한 카페라면
        return

    dessert[arr[x][y]] = True

    if d == 0 or d == 1: # 오른쪽 방향 그대로 가거나 왼쪽으로 꺾었을 경우에
        dfs(x + dx[d], y + dy[d], l + 1, d)
        # d+1 방향
        dfs(x + dx[d + 1], y + dy[d + 1], l + 1, d + 1)
    elif d == 2:
        if sx + sy != x + y:  # 출발점 방향이 아님
            dfs(x + dx[d], y + dy[d], l + 1, d)
        else:
            dfs(x + dx[d + 1], y + dy[d + 1], l + 1, d + 1)
    # d가 3일때는 직진
    else:
        dfs(x + dx[d], y + dy[d], l + 1, d)

    dessert[arr[x][y]] = False

answer = 0
sx, sy = 0, 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            sx, sy = i, j
            dfs(i, j, 0, 0)

    if answer == 0:
        answer = -1
    print('#{} {}'.format(tc, answer))