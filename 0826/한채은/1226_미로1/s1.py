from pprint import pprint
import sys
sys.stdin = open("input.txt")
'''
1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점
'''
def bfs(end):
    di = [-1, 0, 1, 0]  # 사방 탐색하기 위해
    dj = [0, 1, 0, -1]  # 좌표 설정해놓음

    q = []  # 가기로 한 장소를 append 해놓기

    i, j = end[0], end[1] # 시작지점 (도착지를 시작점으로 본 뒤 출발)
    q.append([i, j])     # 빈 q에다가 i와 j의 시작점을 append 함
    while q:    # 만약 q가 있으면
        i, j = q.pop(0)     # 내가 가기로 한 장소를 보려고 pop
        for k in range(4):  # 사방탐색 시작
            ni = i+di[k]    # newi(새로운 좌표)는 기존i에서 사방탐색 범위 더한 좌표
            nj = j+dj[k]    # newj는 기존j에서 사방탐색 범위 더한 좌표
            if 0 <= ni < 16 and 0 <= nj < 16:    # 범위를 벗어나는걸 방지하기 위해 범위설정
                if visited[ni][nj] == 0:    # 아직 방문 하지 않았고
                    if maze[ni][nj] == 2:   # 미로의 좌표가 2면
                        return 1            # 1을 return (도착했음)

                    elif maze[ni][nj] == 0:  # 지도에 길이 나있으면
                        q.append([ni, nj])   # 갈 수 있는 길만 append
                        visited[ni][nj] = 1  # 갔다고 표시해주기
    return 0


for tc in range(1):  # 10개의 테스트케이스 돌면서
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]   # 만들어져 있는 maze 받아오기
    visited = [[0] * 16 for _ in range(16)]  # 내가 방문한 곳을 만들어 놓을 빈 리스트
    # pprint(maze)

    for i in range(16):  # 16 * 16 배열이니까 2차원 배열 만들어서 이거 순회하면서
        for j in range(16):
            if maze[i][j] == 3:  # 만약에 maze의 i,j의 좌표가 3이면 도착
                end = (i, j)     # 도착 지점인 end의 좌표는 i, j

    # pprint(visited)
    print('#{} {}'.format(tc, bfs(end)))