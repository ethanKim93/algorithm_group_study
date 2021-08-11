import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    # IF N = 4 -> 시작 4칸(우) -> 3칸 2번(아래,좌) -> 2칸 2번(위,우) -> 1칸 2번(아래, 좌)
    # move_len = [4, 3, 3, 2, 2, 1, 1]
    move_len = [N]
    while N > 1:
        move_len.extend([N - 1, N - 1])
        N -= 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    num = 1
    x, y, k = -1, 0, 0
    for move in move_len:
        for m in range(move):
            x += dx[k]
            y += dy[k]
            snail[y][x] = num
            num += 1
        k = (k+1)%4

    print('#{}'.format(tc))
    for snail_row in snail:
        print(*snail_row)