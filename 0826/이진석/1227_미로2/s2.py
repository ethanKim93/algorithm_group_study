'''
DFS
'''
import sys

sys.stdin = open('input.txt')


def DFS(start):
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우
    stack = [start]
    visited[start[0]][start[1]] = 1
    while stack:
        now = stack.pop()  # 현재 정점 pop
        i = now[0]
        j = now[1]
        maze[i][j] = 1  # 현재 정점을 1로 갱신해서 다시 검사하지 않도록한다.
        for k in range(4):  # 현재 위치의 상,하,좌,우 검사
            ni = i + d[k][0]
            nj = j + d[k][1]
            if 0 <= ni < 100 and 0 <= nj < 100:  # 인덱스 유효성 검사
                if maze[ni][nj] == 3:  # 도착지점 도착시 True(1) 리턴
                    return 1
                elif maze[ni][nj] == 0:  # 미로의 통로이면서 방문하지 않은 곳일때
                    stack.append([ni, nj])  # 인접 정점 enQ

    return 0


for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, list(input()))) for _ in range(100)]  # 미로 초기화
    visited = [[0] * 100 for _ in range(100)]  # 방문기록 초기화
    for i in range(100):  # 시작지점 찾기
        for j in range(100):
            if maze[i][j] == 2:
                s = [i, j]

    print('#{} {}'.format(tc, DFS(s)))