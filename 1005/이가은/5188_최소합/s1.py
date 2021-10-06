import sys
sys.stdin = open('sample_input.txt')

dy = [1, 0]
dx = [0, 1]

def detect(y, x):
    global ans, temp

    if temp > ans:      # 시간초과 나지 않도록
        return

    if x == N-1 and y == N-1:
        ans = temp
        return

    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or ny >= N:
                continue

            if (ny, nx) not in visited:
                visited.append((ny,nx))
                temp += li[ny][nx]
                detect(ny, nx)
                temp -= li[ny][nx]   # 원복
                visited.remove((ny,nx))

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    li = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    temp = li[0][0]

    ans = 999999
    detect(0, 0)
    print('#{} {}'.format(tc, ans))