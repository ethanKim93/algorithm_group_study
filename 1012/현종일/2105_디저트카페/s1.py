import sys
sys.stdin = open("sample_input.txt")

def search(ii, jj, dir, path):
    global max_eat

    if dir < 2:
        if 0 <= ii + x[dir] < n and 0 <= jj + y[dir] < n:
            if road[ii + x[dir]][jj + y[dir]] not in path:
                search(ii + x[dir], jj + y[dir], dir, path + [road[ii + x[dir]][jj + y[dir]]])
            else:
                search(ii, jj, dir + 1, path)
        search(ii, jj, dir + 1, path)

    elif dir == 2:
        if 0 <= ii + x[dir] < n and 0 <= jj + y[dir] < n:
            if road[ii + x[dir]][jj + y[dir]] not in path:
                if ii + x[dir] - start[0] == jj + y[dir] - start[1]:
                    search(ii + x[dir], jj + y[dir], dir + 1, path + [road[ii + x[dir]][jj + y[dir]]])
                else:
                    search(ii + x[dir], jj + y[dir], dir, path + [road[ii + x[dir]][jj + y[dir]]])
            else:
                return
        else:
            return
    else:
        if ii + x[dir] != start[0]:
            if road[ii + x[dir]][jj + y[dir]] not in path:
                search(ii + x[dir], jj + y[dir], dir, path + [road[ii + x[dir]][jj + y[dir]]])
            else:
                return
        else:
            if len(path) != 1:
                if len(path) > max_eat:
                    max_eat = len(path)
    return


x = [1, 1, -1, -1]
y = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, 1 + T):
    n = int(input())
    road = [list(map(int, input().split())) for _ in range(n)]
    max_eat = -1

    for i in range(n - 1):
        for j in range(1, n - 1):
            start = [i, j]
            search(i, j, 0, [road[i][j]])

    print('#{} {}'.format(tc, max_eat))