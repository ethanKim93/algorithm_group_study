import sys
sys.stdin = open('input.txt')


def dfs(x, y):
    global result
    if map_list[y][x] == 3 or result:
        result = 1
        return
    for i, j in moving:
        dx = x + j
        dy = y + i
        if result:
            return
        if map_list[dx][dy] != 1:
            map_list[x][y] = 1
            dfs(dx, dy)


for _ in range(10):
    tc = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(16)]
    result = 0
    moving = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    dfs(1, 1)
    print('#{} {}'.format(tc, result))