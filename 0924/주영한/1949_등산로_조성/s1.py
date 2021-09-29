import sys
sys.stdin = open("sample_input.txt")

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
max_length = 0


def go(row, col, temp_length, flag):
    global maps, visited, max_length
    stop = True
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col]:
            # 이동할 수 있을 경우 그냥 이동한다.
            if maps[row][col] > maps[new_row][new_col]:
                visited[new_row][new_col] = 1
                go(new_row, new_col, temp_length + 1, flag)
                visited[new_row][new_col] = 0
                stop = False
            # 이동할 수 없는 경우 공사가 가능한지 확인한다.
            else:
                if flag:
                    # 공사가 가능할 때는 직전의 높이에서 1만큼 낮게 깎는 것으로 처리한다.
                    if maps[row][col] > maps[new_row][new_col] - K:
                        temp = maps[new_row][new_col]
                        maps[new_row][new_col] = maps[row][col] - 1
                        visited[new_row][new_col] = 1
                        go(new_row, new_col, temp_length + 1, False)
                        visited[new_row][new_col] = 0
                        maps[new_row][new_col] = temp
                        stop = False

    if stop:
        max_length = temp_length if temp_length > max_length else max_length


T = int(input())
for tc in range(1, T + 1):
    max_length = 0
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for __ in range(N)]

    max_height = 0

    # 가장 높은 지점에 대한 리스트를 구한다.
    max_height_list = []
    for row in range(N):
        for col in range(N):
            if maps[row][col] > max_height:
                max_height_list.clear()
                max_height_list.append([row, col])
                max_height = maps[row][col]
            elif maps[row][col] == max_height:
                max_height_list.append([row, col])
            else:
                continue

    # 가장 높은 지점들에 대해 가장 멀리 갈 수 있는 등산로를 확인한다.
    for max_height in max_height_list:

        temp_row = max_height[0]
        temp_col = max_height[1]

        visited[temp_row][temp_col] = 1
        go(temp_row, temp_col, 1, True)
        visited[temp_row][temp_col] = 0

    print("#{} {}".format(tc, max_length))