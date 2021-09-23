import sys
sys.stdin = open('input.txt')

# 출발지 찾기
def find_start(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                return i, j

def bfs(si, sj):
    q = [[si, sj]]
    visited = [[0] * 16 for _ in range(16)]
    visited[si][sj] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while q:
        t = q.pop(0)
        ti = t[0]
        tj = t[1]
        for k in range(4):
            if 0 <= ti + di[k] < 16 and 0 <= tj + dj[k] < 16:  # maze 안에 있어야함
                if visited[ti + di[k]][tj + dj[k]] == 0:  # 방문하지 않은 칸일 때 이동
                    if maze[ti + di[k]][tj + dj[k]] == '0':
                        q.append([ti + di[k], tj + dj[k]])
                        visited[ti + di[k]][tj + dj[k]] = visited[ti][tj] + 1
                    elif maze[ti + di[k]][tj + dj[k]] == '3':  # 3 찾자마자 return
                        return 1
    return 0


T = 10

for tc in range(1, T+1):
    tc = int(input())
    maze = [list(input()) for _ in range(16)]  # 내용 str임
    si, sj = find_start(maze)
    print('#{} {}'.format(tc, bfs(si, sj)))
