import sys

sys.stdin = open('sample_input.txt')

delta = [(-1, 1), (1, 1), (1, -1), (-1, -1)]  # 1시, 5시, 7시, 11시

def search(r, c, start, dir):
    global max_visit
    if dir == 3 and (r, c) == start:
        if sum(visited) > max_visit:
            max_visit = sum(visited)
            return

    if r < 0 or r >= N or c < 0 or c >= N or visited[cafe[r][c]]:
        return

    visited[cafe[r][c]] = 1
    nr, nc = r + delta[dir % 4][0], c + delta[dir % 4][1]
    search(nr, nc, start, dir)
    if dir != 3:
        nr, nc = r + delta[(dir+1) % 4][0], c + delta[(dir+1) % 4][1]
        search(nr, nc, start, dir+1)
    visited[cafe[r][c]] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    max_visit = -1
    visited = [0] * 101
    for i in range(N - 1):
        for j in range(N - 2):
            search(i, j, (i, j), 0)
            stack.clear()
    print('#{} {}'.format(tc, max_visit))