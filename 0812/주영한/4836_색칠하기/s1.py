import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):

    # 10 x 10 격자를 grid 에 배치한다.
    grid = [[0] * 10 for _ in range(10)]

    # color_set[0] = red_box 정보에 대한 리스트, color_set[1] = red_box 의 수
    # color_set[2] = blue_box 정보에 대한 리스트, color_set[3] = blue_box 의 수
    color_sets = [[], 0, [], 0]

    # 박스의 정보가 몇개 들어오는지를 num_boxes 에 대입한다.
    num_boxes = int(input())

    for i in range(num_boxes):
        # 박스의 정보를 temp_list 에 임시 저장한다.
        temp_list = list(map(int, input().split()))

        # 빨간색으로 칠해지면 정보를 color_sets[0]에 저장하고,
        # 빨간색 박스의 수를 color_sets[1]에 추가해준다.
        # 파란색으로 칠해지면 정보를 color_sets[2]에 저장하고,
        # 파란색 박스의 수를 color_sets[3]에 추가해준다.
        if temp_list[-1] == 1:
            color_sets[0].append(temp_list)
            color_sets[1] += (temp_list[2] - temp_list[0] + 1) * (temp_list[3] - temp_list[1] + 1)
        else:
            color_sets[2].append(temp_list)
            color_sets[3] += (temp_list[2] - temp_list[0] + 1) * (temp_list[3] - temp_list[1] + 1)

    for idx, color_set in enumerate(color_sets):
        # 박스의 수를 나타내는 경우를 무시한다.
        if idx % 2:
            continue

        # idx = 0일 경우는 빨간 박스, idx = 2일 경우는 파란 박스를 의미하고,
        # 각 색이 나타내는 수를 coloring 에 대입하고, 색칠을 실시한다.
        coloring = 1 if idx == 0 else 2
        for box in color_set:
            for row in range(box[0], box[2] + 1):
                for col in range(box[1], box[3] + 1):
                    grid[row][col] += coloring

    result = 0
    # 더 적은 요소를 가진 색깔을 찾는다.
    small_case = 0 if color_sets[1] < color_sets[3] else 2

    # 더 적은 요소를 가진 색깔의 박스들 내부에서 1 + 2로 보라색(3)인 박스의 숫자를 센다
    for box in color_sets[small_case]:
        for row in range(box[0], box[2] + 1):
            for col in range(box[1], box[3] + 1):
                if grid[row][col] == 3:
                    result += 1

    print("#{} {}".format(tc, result))