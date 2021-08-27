import sys
sys.stdin = open('sample_input.txt')
def BFS(start):
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상, 하, 좌, 우
    q = [start]
    while q:
        now = q.pop(0)                                           # 현재위치 deQ
        vi = now[0]
        vj = now[1]
        for k in range(4):                                       # 상,하, 좌, 우 네 방향을 확인하면서 미로의 통로를 점검
            wi = vi + d[k][0]
            wj = vj + d[k][1]
            if 0 <= wi < len(maze) and 0 <= wj < len(maze):
                if maze[wi][wj] == 3:                            # 도착지점이라면 이제까지의 이동경로 반환
                    return road[vi][vj]
                else:                                            # 도착지점이 아닐 때
                    if not maze[wi][wj] and not road[wi][wj]:    # 미로의 통로면서 경로 확인을 안했을 때
                        q.append([wi, wj])                       # 좌표 enQ
                        road[wi][wj] = road[vi][vj] + 1          # start에서 부터 현재 미로의 통로 까지의 경로 칸수 저장
    return 0
for tc in range(1, int(input())+1):
    N = int(input())
    maze = []                               # 미로
    road = [[0]*N for n in range(N)]        # 거리를 확인하기 위한 배열
    for _ in range(N):                      # 미로 초기화
        maze.append(list(map(int,list(input()))))

    for i in range(N):                      # 시작지점 찾기
        for j in range(N):
            if maze[i][j] == 2:
                s = [i, j]  # 시작지점

    print('#{} {}'.format(tc, BFS(s)))