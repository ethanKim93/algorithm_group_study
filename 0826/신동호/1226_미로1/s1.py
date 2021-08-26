import sys
from pprint import pprint
sys.stdin = open('input.txt')

#5105 코드 거의 그대로 쓰기..ㅎ

def maze(matrix, ni, nj, dist): # 현재 좌표를 기준으로 거리 path에 저장하고 상 하 좌 우로 다시 돌려주는 함수
    path[ni][nj] = dist # 현재 거리 저장
    for m in range(4): # 상, 하, 좌, 우를 m이라는 모드로 표현
        mi = ni + di[m]  # 모드 별 행 값
        mj = nj + dj[m] # 모드 별 열 값
        if 0 <= mi < N and 0 <= mj < N and not matrix[mi][mj] in [1,2]: # 벽이나 시작점인 경우 제외 (시작점 제외 안해주면 path가 2가 됨)
            if not path[mi][mj]: # path가 비어있는 경우 채워줌
                maze(matrix, mi, mj, dist + 1) # 거리 1 늘려서 다시 확인
            elif path[mi][mj] > dist + 1: # 만약 기존의 path 거리보다 지금 거리가 짧으면 업데이트
                maze(matrix, mi, mj, dist + 1)

T = 10 # 테스트 케이스 개수

for tc in range(1, T+1):
    n = int(input())
    N = 16 # 미로 크기
    matrix = [list(map(int, list(input()))) for _ in range(N)] # 미로 모양
    path = [[0] * N for _ in range(N)] # 시작점 기준 거리 저장할 행렬
    di = [-1, 1, 0, 0] # 상, 하, 좌, 우 행
    dj = [0, 0, -1, 1] # 상, 하, 좌, 우 열
    dist = 0 # 거리 0으로 시작
    for i in range(N): # 시작점 찾기
        for j in range(N):
            if matrix[i][j] == 2:
                si, sj = i, j # 시작점 좌표 저장
    maze(matrix, si, sj, dist) # 시작점 기준으로 미로 돌면서 path에 거리 저장
    for i in range(N): # 도착점 찾기
        for j in range(N):
            if matrix[i][j] == 3:
                arrive = path[i][j] # 도착점 거리 저장
    if not arrive: # 0인 경우 도착 안했으므로 그대로 0 출력
        print('#{} {}'.format(tc, arrive))
    else: # 성공시 1 출력
        print('#{} 1'.format(tc))