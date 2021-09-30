import sys
sys.stdin = open("sample_input.txt")

delta_x = [0, 0, -1, 1]
delta_y = [-1, 1, 0, 0]

def highest():
    point = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if point < matrix[i][j]:
                point = matrix[i][j]

    return point

def route(height, lose):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == height:
                tracking(y, x, lose)
    return

def tracking(y, x, lose):
    global result
    stack.append((y, x))

    for idx in range(4):
        dirt_y = y + delta_y[idx]
        dirt_x = x + delta_x[idx]

        if 0 <= dirt_x < len(matrix) and 0 <= dirt_y < len(matrix) and (dirt_y, dirt_x) not in stack:
            if matrix[y][x] > matrix[dirt_y][dirt_x]:
                tracking(dirt_y, dirt_x, lose)

            elif lose and matrix[y][x] > matrix[dirt_y][dirt_x] - K:
                tmp = matrix[dirt_y][dirt_x]
                matrix[dirt_y][dirt_x] = matrix[y][x] - 1
                tracking(dirt_y, dirt_x, False)
                matrix[dirt_y][dirt_x] = tmp
    stack.pop()

    result = result if result > len(stack) else len(stack) + 1

T = int(input())
for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    stack = []
    result = 0
    height = highest()
    route(height, True)
    print("#{} {}".format(tc,result))