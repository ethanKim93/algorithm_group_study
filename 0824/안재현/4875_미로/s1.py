def search(lst, x, y, check):
    global is_check
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for l in range(4):
        xx = x + dx[l]
        yy = y + dy[l]
        if 0 <= xx < len(lst) and 0 <= yy < len(lst) and not check[xx][yy]:
            check[xx][yy] = True
            if lst[xx][yy] == 3:
                is_check = True
            elif lst[xx][yy] == 0:
                search(lst, xx, yy, check)


T = int(input())
for i in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    wall = [[False for _ in range(N)] for i in range(N)]
    is_check = False
    for j in range(N):
        for k in range(N):
            if maze[j][k] == 2:
                search(maze, j, k, wall)
    if is_check:
        print("#{} 1".format(i + 1))
    else:
        print("#{} 0".format(i + 1))