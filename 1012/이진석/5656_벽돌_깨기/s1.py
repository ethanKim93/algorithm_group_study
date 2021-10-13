import sys
import copy

sys.stdin = open('sample_input.txt')
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우


def DFS(cnt, arr):
    global min_brick
    if cnt == N:                # 구슬을 다 쐈으면 종료
        brick = 0
        for i in range(W):      # 남은 벽돌의 갯수를 세고, 최소값 갱신
            for j in range(H):
                if arr[j][i]:
                    brick += 1
                if brick >= min_brick:
                    return
        if min_brick > brick:
            min_brick = brick
            return

    for col in range(W):        # 발사할 열 정하기
        for row in range(H):    # 발사할 행 찾기 > 가장 위에있는 벽돌이 맞아야 하기때문
            if arr[row][col]:   # 발사할 행을 찾았으면
                temp_arr = copy.deepcopy(arr)   # 벽돌이 깨지면 배열이 변경되기 때문에 임시 배열에 deepcopy
                breaking(row, col, temp_arr)    # 벽돌 깨기
                renewal(temp_arr)               # 꺤 벽돌 갱신(아래로 내리기)
                DFS(cnt + 1, temp_arr)          # DFS
                break                           # 다음 행을 점검하지 않게 하기 위해 break
    DFS(N, arr)                                 # 모든 배열을 돌았지만, 벽돌이 남아있지 않을 때 종료시키기


def breaking(r, c, arr):        # 벽돌 제거
    size = arr[r][c] - 1        # 자기자신을 제외하고 네 방향으로 터트릴 크기
    arr[r][c] = 0               # 현재 자리 벽돌 터트리기
    if size < 1: return arr     # 현재 자리가 0, 1일때 종료
    for d in delta:
        nr, nc = r, c           # 새로운 행,열
        temp = size             # 크기 복사(네 방향으로 모두 확인해야 하기 때문)
        while temp != 0:        # 크기만큼 벽돌 터트리기(breaking 재귀)
            nr = nr + d[0]
            nc = nc + d[1]
            if 0 <= nr < H and 0 <= nc < W and arr[nr][nc]:
                breaking(nr, nc, arr)
            temp -= 1
    return arr


def renewal(arr):  # 벽돌 아래로 내리기 (사이의 0 제거)
    for i in range(W):
        for j in range(H - 1, -1, -1):                      # 아래에서 위로 올라가면서
            if not arr[j][i]:                               # 가장 처음 0을 만났을 때
                for k in range(j - 1, -1, -1):
                    if arr[k][i]:                           # 0보다 위에있는 벽돌과 자리 교체
                        arr[k][i], arr[j][i] = arr[j][i], arr[k][i]
                        break
    return arr


for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())  # N : 구슬갯수, W : 가로, H : 세로
    table = [list(map(int, input().split())) for _ in range(H)]  # 벽돌 배열
    min_brick = W * H  # 남은 벽돌

    DFS(0, table)
    print('#{} {}'.format(tc, min_brick))
