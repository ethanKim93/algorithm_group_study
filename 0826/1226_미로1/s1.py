import sys
sys.stdin = open('input.txt')

def DFS(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16: # 델타 조건
                if maps[nx][ny] == '0':       # 길을 만날 경우
                    stack.append((nx, ny))
                    maps[nx][ny] = '-1'
                elif maps[nx][ny] == '3':     # 도착점을 만날 경우
                    return 1                  # 1 리턴
    return 0       #도착하지 못한경우 0 리턴

for _ in range(10):
    n = int(input())
    maps = [list(input()) for _ in range(16)]

    # 출발점 찾기
    x, y = 0, 0
    for i in range(16):
        for j in range(16):
            if maps[i][j] == '2':       # 시작점 찾아줌
                x, y = i, j

    print('#{} {}'.format(n, DFS(x,y)))
