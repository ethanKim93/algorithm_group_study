import copy

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def splash(a, b, A):
    if A[a][b]:
        area = A[a][b]
        A[a][b] = 0
    else:
        return
    for i in range(area):
        for x in range(4):
            di = a + dx[x] * i
            dj = b + dy[x] * i
            if 0 <= di < H and 0 <= dj < W:
                splash(di, dj, A)


def down(A):
    for a in range(W):
        for i in range(H - 1, -1, -1):
            if not A[i][a]:
                for j in range(i, -1, -1):
                    if A[j][a]:
                        A[i][a] = A[j][a]
                        A[j][a] = 0
                        break


def counter(A):
    dol = 0
    for j in range(W):
        for i in range(H - 1, -1, -1):
            if not A[i][j]:
                break
            else:
                dol += 1
    return dol


def backtracking(n, A):
    global max_break
    if n == N:
        max_break = min(max_break, counter(A))
        return
    for j in range(W):
        tmp = copy.deepcopy(A)
        for i in range(H):
            if tmp[i][j]:
                splash(i, j, tmp)
                down(tmp)
                backtracking(n + 1, tmp)
                tmp = copy.deepcopy(A)
                break


for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    max_break = 1000
    backtracking(0, arr)
    if max_break == 1000:
        max_break = 0
    print('#{} {}'.format(tc, max_break))