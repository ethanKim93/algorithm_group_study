import sys
sys.stdin = open('sample_input.txt')

from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def BFS():
    while queue:
        row, col = queue.popleft()
        for to in range(4):
            y = row + dy[to]
            x = col + dx[to]

            if 0 <= y < N and 0 <= x < N:
                more_energy = field[y][x] - field[row][col] if field[row][col] < field[y][x] else 0
                new_val = val[row][col] + 1 + more_energy
                if val[y][x] > new_val:
                    val[y][x] = new_val
                    queue.append((y, x))


for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    val = [[N * N] * N for _ in range(N)]
    val[0][0] = 0
    queue = deque()
    queue.append((0, 0))
    BFS()

    print("#{} {}".format(case + 1, val[-1][-1]))