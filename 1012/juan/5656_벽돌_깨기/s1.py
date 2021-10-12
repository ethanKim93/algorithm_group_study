T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def gravity(arr):                                   # 폭발 끝나고 공중에 떠있는 벽돌들 아래로 내려서 정리하기
    for c in range(W):
        s = []
        for r in range(H):
            if arr[r][c]:                           # 숫자가 들어있는 벽돌을
                s.append(arr[r][c])                 # 스택에 넣고
                arr[r][c] = 0                       # 해당위치는 0으로
        h = H-1
        while s:
            arr[h][c] = s.pop()                     # 스택에서 하나씩 꺼내서 해당 열의 바닥부터 다시 채워 올림
            h -= 1


def shot(row, col, new_arr):
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if new_arr[r][c] > 1:                       # 연쇄 폭발하는 벽돌인지
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                for j in range(new_arr[r][c] - 1):  # 연쇄 폭발로 폭발하는 벽돌 중 연쇄 폭발하는 벽돌은 스택에 추가
                    if 0 <= nr < H and 0 <= nc < W:
                        if new_arr[nr][nc] > 1:
                            stack.append((nr, nc))
                        else:
                            new_arr[nr][nc] = 0
                        nr, nc = nr + dr[i], nc + dc[i]
                    else:
                        break
        new_arr[r][c] = 0
    gravity(new_arr)


def remains(arr):                                   # 남은 벽돌 세는 함수
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
    if idx == N:                                    # 구슬 다 던졌으면
        res = remains(arr)
        if res < bricks:                            # 남은 벽돌과 현재 벽돌 최솟값 비교
            bricks = res
        return

    for c in range(W):
        new_arr = [list(arr[_]) for _ in range(H)]
        for r in range(H):
            if new_arr[r][c]:                       # 깰 벽돌이 있는 열에서
                shot(r, c, new_arr)                 # 구슬 투하
                if not remains(new_arr):            # 구슬 투하하고 남은 벽돌없으면 벽돌 최솟값 0 할당 후 리턴
                    bricks = 0
                    return
                dfs(idx+1, new_arr)                 # 남은 벽돌 있으면 다시 DFS
                break


for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(H)]
    bricks = 987654321
    dfs(0, base)
    print('#{} {}'.format(tc, bricks))