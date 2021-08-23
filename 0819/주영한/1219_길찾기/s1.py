import sys
sys.stdin = open("input.txt")


def dfs(matrix, visited, start, end):
    move_stack = []
    visited[start] = 1
    for i in range(100):
        if matrix[start][i] == 1 and not visited[i]:
            move_stack.append(i)

    while move_stack:
        new_start = move_stack.pop()
        for i in range(100):
            if matrix[new_start][i] == 1 and not visited[i]:
                if i == end:
                    return 1
                visited[i] = 1
                move_stack.append(i)
    return 0


for tc in range(1, 11):
    dum, N = map(int, input().split())
    move_table = list(map(int, input().split()))

    matrix = [[0] * 100 for _ in range(100)]
    visited = [0] * 100

    for idx in range(0, len(move_table), 2):
        matrix[move_table[idx]][move_table[idx + 1]] = 1
    print("#{} {}".format(tc, dfs(matrix, visited, 0, 99)))