import sys
sys.stdin = open('sample_input.txt')


def rec(u, v, k, cnt):
    global max_cnt
    if k == 3 and (u, v) == stop:  # 우상방향이고 출발점에 도착했을때
        max_cnt = max(max_cnt, cnt)
    elif not 0 <= u < N or not 0 <= v < N:  # area를 벗어나는지 확인
        return
    elif area[u][v] in queue:  # 중복 숫자가 존재하는지
        return
    else:
        queue.append(area[u][v])  # 숫자 삽입
        nx, ny = u + dx[k], v + dy[k]  # 방향적용한 새로운 nx,ny
        if k != 3:  # 방향이 우하, 좌하, 좌상 인경우
            rec(nx, ny, k, cnt+1)  # 쭉 그대로 진행
            rec(u + dx[k+1], v + dy[k+1], k+1, cnt +1)  # 방향 전환
        else:  # 방향이 우상
            rec(nx, ny, k, cnt+1)  # 뱡향전환 필요없이 진행
        queue.remove(area[u][v])  # queue초기화 작업


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = -1
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    queue = []
    for i in range(N):
        for j in range(1, N - 1):
            stop = (i, j)
            queue.append(area[i][j])
            rec(i+1, j+1, 0, 1)
            queue.remove(area[i][j])
    print('#{} {}'.format(tc, max_cnt))
