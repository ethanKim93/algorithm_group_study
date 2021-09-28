import sys
sys.stdin = open('input.txt')

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# pipe가 8개인 이유 : 0번 인덱스로 하지 않고 편하게 가려고
pipe = [
    [0, 0, 0, 0], # 사용 안함
    [1, 1, 1, 1],  # 상하좌우
    [0, 1, 0, 1],  # 상하
    [1, 0, 1, 0],  # 좌우
    [1, 0, 0, 1],  # 상우
    [1, 1, 0, 0],  # 하우
    [0, 1, 1, 0],  # 하좌
    [0, 0, 1, 1],  # 상좌
]

for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    # 지도 정보 입력
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]       #시간 및 방문 여부 확인
    Q = [(R, C)] #초기값 설정
    visited[R][C] = 1
    ans = 0

    while Q:
        r, c = Q.pop(0)
        ans += 1

        if visited[r][c] >= L:
            continue
        # 네 방향 탐색 시작
        for d in  range(4):
            curr_p = tunnel[r][c]
            # 연결이 안된다면 컨티뉴
            if pipe[tunnel[r][c]][d] == 0:
                continue

            nr = r + dr[d]
            nc = c + dc[d]

            # 좌표가 맵을 벗어나면 컨티뉴
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue


            nd = (d+2) % 4
            np = tunnel[nr][nc]

            # 방문 or 다음 좌표 파이프가 현재 좌표와 연결되지 않는다면 컨티뉴
            if visited[nr][nc] or pipe[np][nd] == 0:
                continue

            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))

    print('#{} {}'.format(tc, ans))