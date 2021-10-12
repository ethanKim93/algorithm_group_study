import sys
sys.stdin = open('sample_input.txt')

dirs = [
    [-1, 1],
    [1, 1],
    [1, -1],
    [-1, -1],
]

def dfs(cur_row, cur_col, dir, score, is_rectangle):
    global answer, is_large
    if 0 <= cur_row < N and 0 <= cur_col < N:
        if is_rectangle >= 1 and dir >= 1:
            return
        if score > 0 and cur_row == row and cur_col == col:
            if answer < score:
                answer = score
            return
        if dir == 3 and len(desserts.keys()) * 2 <= answer:
            return
        if desserts.get(brd[cur_row][cur_col]):
            return

        desserts[brd[cur_row][cur_col]] = 1

        dfs(cur_row+dirs[dir][0], cur_col+dirs[dir][1], dir, score+1, is_rectangle)
        if is_rectangle == 0:
            is_rectangle = (dir+1)//4
        dfs(cur_row+dirs[(dir+1)%4][0], cur_col+dirs[(dir+1)%4][1], (dir+1)%4, score+1, is_rectangle)
        del desserts[brd[cur_row][cur_col]]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    brd = [list(map(int, input().split())) for _ in range(N)]
    answer = -1

    for row in range(N):
        for col in range(N):
            desserts = {}
            dfs(row, col, 0, 0, 0)

    print("#{} {}".format(tc, answer))