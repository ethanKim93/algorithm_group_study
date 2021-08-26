import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    temps = [[0] * n for _ in range(n)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(n):
        for x in range(n):
            if maps[i][x] == 2:
                start = [i, x]
            elif maps[i][x] == 3:
                goal = [i, x]
                maps[i][x] = 0


    q = []
    q.append(start)
    temps[start[0]][start[1]] = 1

    # BFS
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dirs[i][0] # 탐색할 row 좌표
            nc = c + dirs[i][1] # 탐색할 col 좌표
            if 0 <= nr < n and 0 <= nc < n: # 좌표상에 있으면
                if maps[nr][nc] == 0 and temps[nr][nc] == 0: # 갈 수 있는 길이고, 지나 간 길이 아니면
                    q.append([nr,nc]) # 다음 장소로 추가
                    temps[nr][nc] = temps[r][c] + 1 # 해당 좌표까지의 최단거리 기록

    # goal을 못 갈경우 예외처리
    if temps[goal[0]][goal[1]] == 0:
        temps[goal[0]][goal[1]] = 2

    print("#{} {}".format(tc,temps[goal[0]][goal[1]]-2)) # 0을 지난 횟수: -1, 시작점이 1: -1 -> -2