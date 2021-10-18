import sys
sys.stdin = open('input.txt')

def BFS(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = [(x, y)]

    while queue:
        a, b = queue.pop(0)
        for i in range(4):
            vx = a + dx[i]
            vy = b + dy[i]
            if vx >= 0 and vx < N and vy >= 0 and vy < N:
                if new_matrix[a][b] + matrix[vx][vy] < new_matrix[vx][vy]:
                    new_matrix[vx][vy] = new_matrix[a][b] + matrix[vx][vy]
                    queue.append((vx, vy))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for i in range(N)]
    new_matrix = [[987654321]*N for i in range(N)]
    new_matrix[0][0] = 0
    BFS(0,0)
    print('#{} {}'.format(tc, new_matrix[-1][-1]))