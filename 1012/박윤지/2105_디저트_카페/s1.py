import sys
sys.stdin = open('sample_input.txt')

# 왼위, 오위, 왼아, 오아
dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]

# 출발한 카페로 돌아와야 한다.
# 하나의 카페에서 디저트를 먹는 것도 안 된다
# 사각형을 만들어야함 -> i를 0,1,2,3 다 써야함
def move(r, c):
    global ans, total
    # 출발점은 visited에 표시 안함
    if 0 in direction and 1 in direction and 2 in direction and 3 in direction:
        if ans < total:
            ans = total

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and cafe[nr][nc] not in desert:
            visited[nr][nc] = 1
            desert.append(cafe[nr][nc])
            direction.append(i)
            total += cafe[nr][nc]
            move(nr, nc)
            visited[nr][nc] = 0
            desert.remove(cafe[nr][nc])
            direction.remove(i)
            total -= cafe[nr][nc]



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    desert = []  # 지금까지 먹은 디저트 숫자
    direction = []
    ans = 0
    total = 0
    for i in range(N):
        for j in range(N):
            if (i, j) not in [(0,0), (0,N-1), (N-1,0), (N-1,N-1)]:
                move(i, j)
    print(ans)
