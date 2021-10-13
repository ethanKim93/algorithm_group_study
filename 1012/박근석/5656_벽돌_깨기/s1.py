import sys
sys.stdin = open('input.txt')

T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def gravity(arr):
    for c in range(W):
        s = []
        for r in range(H):
            if arr[r][c]:
                s.append(arr[r][c])
                arr[r][c] = 0
        h = H-1
        while s:
            arr[h][c] = s.pop()
            h -= 1


def shot(row, col, arr1):
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if arr1[r][c] > 1:
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                for j in range(arr1[r][c] - 1):
                    if 0 <= nr < H and 0 <= nc < W:
                        if arr1[nr][nc] > 1:
                            stack.append((nr, nc))
                        else:
                            arr1[nr][nc] = 0
                        nr, nc = nr + dr[i], nc + dc[i]
                    else:
                        break
        arr1[r][c] = 0
    gravity(arr1)

def remains(arr):
    cnt = 0
    for c in range(W):
        for r in range(H-1, -1, -1):
            if not arr[r][c]:
                break
            cnt += 1
    return cnt

def dfs(idx, arr):
    global bricks
    if not bricks:
        return
    if idx == N:
        res = remains(arr)
        if res < bricks:
            bricks = res
        return

    for w in range(W):
        arr1 = [list(arr[_]) for _ in range(H)]
        for h in range(H):
            if arr1[h][w]:
                shot(h, w, arr1)
                if not remains(arr1):
                    bricks = 0
                    return
                dfs(idx+1, arr1)
                break

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(H)]
    bricks = 987654321
    dfs(0, matrix)
    print('#{} {}'.format(tc, bricks))

