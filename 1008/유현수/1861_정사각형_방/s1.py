import sys
sys.stdin = open('input.txt')


def move(r, c, cnt, start_num):
    global max_cnt, min_start_num
    flag = 0                # 4방향 모두 갈 수 없는 상태인지를 확인하는 플래그
    for d in range(4):      # 4방향 순회
        nr = r + dr[d]
        nc = c + dc[d]
        # 방 범위 이내이면서 딱 1만큼 큰 수가 있는지 탐색하고 이동
        if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] - matrix[r][c] == 1:
            move(nr, nc, cnt+1, start_num)
        else:                           # 해당 방향으로 없다면
            flag += 1                   # 플래그 1 추가

    # 4방향 모두 갈 수 없고
    # 현재 이동 횟수가 최대 이동 횟수보다 크다면 업데이트
    if flag == 4 and max_cnt < cnt:
        max_cnt = cnt
        min_start_num = start_num

    # 현재 이동 횟수가 최대 이동 횟수와 같으면 방 번호 비교
    elif flag == 4 and max_cnt == cnt:
        if min_start_num > start_num:
            min_start_num = start_num


dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0             # 가장 많은 이동 횟수
    min_start_num = 0       # 가장 많은 이동이 가능하면서 숫자가 가장 작은 출발지점
    for i in range(N):
        for j in range(N):                  # 방의 모든 위치에서 출발
            move(i, j, 1, matrix[i][j])

    print('#{} {} {}'.format(tc, min_start_num, max_cnt))