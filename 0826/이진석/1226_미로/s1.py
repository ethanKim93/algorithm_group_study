'''
BFS
'''
import sys
sys.stdin = open('input.txt')

def BFS(start):
    d = [[-1, 0],[1, 0],[0, -1],[0, 1]] # 상 하 좌 우
    q = [start]
    visited[start[0]][start[1]] = 1
    while q:
        now = q.pop(0)                          # 현재 정점 deQ
        vi = now[0]
        vj = now[1]
        for k in range(4):                      # 현재 위치의 상,하,좌,우 검사
            wi = vi + d[k][0]
            wj = vj + d[k][1]
            if 0 <= wi < 16 and 0 <= wj < 16:   # 인덱스 유효성 검사
                if maze[wi][wj] == 3:           # 도착지점 도착시 True(1) 리턴
                    return 1
                else:
                    if not maze[wi][wj] and not visited[wi][wj]:    # 미로의 통로이면서 방문하지 않은곳에 도착했을 때
                        q.append([wi, wj])      # 인접 정점 enQ
                        visited[wi][wj] = 1     # 방문 기록

    return 0
for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int,list(input()))) for _ in range(16)]    # 미로 초기화
    visited = [[0]*16 for _ in range(16)]                       # 방문기록 초기화
    for i in range(16):                                         # 시작지점 찾기
        for j in range(16):
            if maze[i][j] == 2:
                s = [i, j]

    print(BFS(s))