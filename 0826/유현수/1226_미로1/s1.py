import sys
sys.stdin = open('input.txt')


def BFS():
    queue = [(1, 1)]
    visited[1][1] = 1
    while queue:
        now = queue.pop(0)
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if maze[nr][nc] == '3':
                return 1
            elif maze[nr][nc] != '1' and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = 1
    return 0


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for _ in range(1, 11):
    tc = int(input())
    maze = [list(input()) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    print('#{} {}'.format(tc, BFS()))
