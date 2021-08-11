import sys
sys.stdin = open('input.txt')

dr = [0, 0, 1, -1]  # (우, 하, 좌, 상 #시계방향)
dc = [1, -1, 0, 0]

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(N):
        for j in range(N):  # 여기까지 모든 좌표에 접근하는 것
            part = 0 # focus를 옮겨갈때마다 초기화되는 임시 합 변수
            for k in range(4):  # range(4) 네 방향에 접근하겠다
                nr = i + dr[k]  # ni 주변 칸의 좌표 i 현재 좌표
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    now = arr[nr][nc] - arr[i][j]
                    if now < 0:
                        now *= -1
                    part += now
            total += part
    print('# {} {}'.format(test_case, total))