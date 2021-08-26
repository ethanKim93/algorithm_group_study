import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 지금까지 bfs로 푼 줄 알았던 1226, 5102, 5105가 dfs인 것 같아서 다시 bfs로 풀어보기

def maze(matrix): # 현재 좌표를 기준으로 거리 path에 저장하고 상 하 좌 우로 다시 돌려주는 함수
    q = [[si,sj]]
    while q:
        v = q.pop(0)
        for m in range(4): # 상, 하, 좌, 우를 m이라는 모드로 표현
            mi = v[0] + di[m]  # 모드 별 행 값
            mj = v[1] + dj[m] # 모드 별 열 값
            if 0 <= mi < N and 0 <= mj < N and not matrix[mi][mj] in [1,2]: # 벽이나 시작점인 경우 제외 (시작점 제외 안해주면 path가 2가 됨)
                if not path[mi][mj]: # path가 비어있는 경우 채워줌
                    path[mi][mj] = path[v[0]][v[1]] + 1
                    q.append([mi,mj])


T = 10 # 테스트 케이스 개수

for tc in range(1, T+1):
    n = int(input())
    N = 100 # 미로 크기
    matrix = [list(map(int, list(input()))) for _ in range(N)] # 미로 모양
    path = [[0] * N for _ in range(N)] # 시작점 기준 거리 저장할 행렬
    di = [-1, 1, 0, 0] # 상, 하, 좌, 우 행
    dj = [0, 0, -1, 1] # 상, 하, 좌, 우 열
    for i in range(N): # 시작점 찾기
        for j in range(N):
            if matrix[i][j] == 2:
                si, sj = i, j # 시작점 좌표 저장
    maze(matrix) # 시작점 기준으로 미로 돌면서 path에 거리 저장
    for i in range(N): # 도착점 찾기
        for j in range(N):
            if matrix[i][j] == 3:
                arrive = path[i][j] # 도착점 거리 저장
    if not arrive:
        print('#{} {}'.format(tc, arrive))
    else:
        print('#{} {}'.format(tc, 1))