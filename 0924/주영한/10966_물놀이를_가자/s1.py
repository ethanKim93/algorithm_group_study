import sys
sys.stdin = open("sample_input.txt")


def BFS():
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = [0] * (N * M)
    front = -1
    rear = -1
    for n in range(N):
        for m in range(M):
            if fields[n][m] == 0:
                rear += 1
                queue[rear] = M * n + m

    while front != rear:
        front += 1
        idx = queue[front]
        row, col = idx // M, idx % M
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0 <= new_row < N and 0 <= new_col < M and fields[new_row][new_col] < 0:
                fields[new_row][new_col] = fields[row][col] + 1
                rear += 1
                queue[rear] = M * new_row + new_col

def cnt():
    result = 0
    for n in range(N):
        for m in range(M):
            if fields[n][m] != 0:
                result += fields[n][m]
    return result


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fields = [list(map(lambda x : ord(x) - ord('W'), input())) for _ in range(N)]
    BFS()
    print("#{} {}".format(tc, cnt()))
