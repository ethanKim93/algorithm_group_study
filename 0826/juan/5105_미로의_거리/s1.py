import sys
sys.stdin = open('sample_input.txt')

T = int(input())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def BFS():
    while move:                                                 # queue 가 비워질 때까지
        r, c = move.pop(0)                                      # queue의 첫번째 항목 dequeue
        for i in range(4):                                      # 4방향 확인
            a = r + dr[i]
            b = c + dc[i]
            if 0 <= a < N and 0 <= b < N and not dist[a][b]:    # 미로의 범위 안에 있으면서 방문해서 거리를 입력한 기록이 없는 좌표 만 확인
                if maze[a][b] == '0':                           # 미로의 해당 좌표값이 '0'이면
                    move.append([a, b])                         # queue에 추가
                    dist[a][b] = dist[r][c] + 1                 # dist에는 이전 좌표에서의 거리값+1 을 입력
                elif maze[a][b] == '3':                         # 미로의 해당 좌표값이 '3'이면
                    return dist[r][c]                           # 이전 좌표에서의 거리값이 지나온 거리 이므로 이를 반환
    return 0                                                    # queue를 다 비울때까지 도착지인 '3'을 만나지 못하면 0 반환

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]                    # 미로 입력
    move = []                                                   # queue 생성
    dist = [[0]*N for _ in range(N)]                            # 지나간 거리값 입력할 2차원 배열 초기화

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                move.append([i,j])                              # 출발지 좌표를 queue에 enqueue
                break                                           # 출발지 찾았으니 반복 종료
    print('#{} {}'.format(tc, BFS()))