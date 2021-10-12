import sys
sys.stdin = open('sample_input.txt')
from collections import deque

def shoot(A, cnt):                                                    # 벽돌 깨는 함수
    global minimum                                                    # 남은 최소 벽돌 수
    if cnt:                                                           # 깰 수 있는 기회가 남음
        for j in range(W):                                            # 모든 위치에서 공 발사
            visited = [[0] * W for _ in range(H)]                     # 깨졌는지 확인
            flag = 0                                                  # 현재 열 벽돌 있는지 flag
            for i in range(H):                                        # 벽돌과 만나는 첫번쨰 높이
                if A[i][j]:                                           # 현재 위치에 벽돌이 있다면
                    q = deque()                                       # 부서지는 벽돌들 q
                    q.append((i, j))
                    while q:                                          # 부서질 벽돌 있다면
                        i, j = q.popleft()
                        if not visited[i][j]:                         # 아직 안깨진 벽돌
                            for sh in range(A[i][j]):                 # 범위만큼
                                for dd in d:                          # 상하좌우
                                    si = sh * dd[0] + i
                                    sj = sh * dd[1] + j
                                    if si in range(H) and sj in range(W) and not visited[si][sj]: # 범위 안에 있고 안깨졌다면
                                        q.append((si, sj))            # 깨질 벽돌 추가
                            visited[i][j] = 1                         # 현재 위치 깨짐 표시
                    arr = arrange(A, visited)                         # 중력에 의한 정돈
                    flag = 1                                          # 현재 열 벽돌 있었음
                    break                                             # 다음 높이 확인할 필요 없음
            if not flag:                                              # 벽돌이 없었다면
                arr = A                                               # 변화 없음
            shoot(arr, cnt-1)                                         # 기회 1 감소
    else:                                                             # 기회 다 씀
        tot = 0                                                       # 남은 벽돌 계산
        for i in range(H):
            for j in range(W):
                if A[i][j]:
                    tot += 1
        if tot < minimum:
            minimum = tot

def arrange(A, visited):                                              # 중력에 의한 정돈 함수
    arr = [[0] * W for _ in range(H)]                                 # 새로 정돈될 행렬
    for j in range(W): 
        height = H - 1                                                # 맨 아래부터 벽돌이 쌓인다
        for i in range(H-1, -1, -1):
            if not visited[i][j]:                                     # 안 꺠진 벽돌이라면 아래서부터 추가
                arr[height][j] = A[i][j]
                height -= 1
    return arr                                                        # 정돈된 행렬 반환


T = int(input())

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]                                # 우, 좌, 하, 상

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(H)]
    minimum = 987654321

    shoot(mat, N)
    print('#{} {}'.format(tc, minimum))
