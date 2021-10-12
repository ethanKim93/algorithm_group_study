import sys
sys.stdin = open('input.txt', 'r')

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
for tc in range(1, int(input())+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    position = [0] * ((N ** 2) + 1)     # 각 숫자의 배열위치
    distance = [0] + [1] * (N ** 2)     # 각 숫자에서 연속된 거리( ex. 5일때 3,4,5연속이라면 dis[5]==3 )
    max_cnt = -1
    roomnum = -1
    for i in range(N):                  # 각 방 번호 오름차순으로 좌표를 position에 입력
        for j in range(N):
            position[rooms[i][j]] = (i, j)

    i = 2
    while i < len(distance):            # 이전 번호의 방의 좌표가 상,하,좌,우에 존재하면 거리 갱신(이전거리 + 1)
        r = position[i][0]
        c = position[i][1]
        for d in delta:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < N and 0 <= nc < N and rooms[r][c] - 1 == rooms[nr][nc]:
                distance[i] += distance[i-1]
                break
        i += 1

    for i in range(1, len(distance)):
        if distance[i] > max_cnt:
            max_cnt = distance[i]
            roomnum = i - distance[i] + 1
    print('#{} {} {}'.format(tc, roomnum, max_cnt))