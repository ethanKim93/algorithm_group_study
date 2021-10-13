import sys
sys.stdin = open('sample_input.txt')

def game(cnt, block):
    global max_break, N

    if cnt == N:
        if broken > max_break:
            max_break = broken
        return

    if broken <= max_break:
        return

    for i in range(W):
        brick_break(i, block)
        game(cnt+1, block)

dy = [-1,1,0,0]
dx = [0,0,-1,0]
def brick_break(i, block):
    power = block[0][i]
    y = 0
    x = i
    while power != 0:
        y += 1
        power = block[y][x]

    for p in range(power):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= nx < W and 0 <= ny < H:
                brick_break(power, block)


T = int(input())

for tc in range(1,T+1):
    # N : N개의 벽돌, W : 가로, H : 세로
    N, W, H = map(int,input().rstrip().split(' '))
    block = [list(map(int,input().split())) for _ in range(H)]
    max_break = 0
