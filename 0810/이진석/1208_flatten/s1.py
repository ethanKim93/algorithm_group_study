import sys

sys.stdin = open('input.txt')


def box_min_max(input_boxes):   # 최대, 최소 박스의 인덱스 반환
    max_box = input_boxes[0]
    max_idx = 0
    min_box = input_boxes[0]
    min_idx = 0
    for j in range(100):
        if max_box < input_boxes[j]:
            max_box = input_boxes[j]
            max_idx = j
        if min_box > input_boxes[j]:
            min_box = input_boxes[j]
            min_idx = j
    return min_idx, max_idx


for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    for i in range(dump):
        boxes[box_min_max(boxes)[1]] -= 1   # 가장 높은 박스 -1
        boxes[box_min_max(boxes)[0]] += 1   # 가장 낮은 박스 +1

    answer = boxes[box_min_max(boxes)[1]] - boxes[box_min_max(boxes)[0]]    # 최대 높이와 최소 높이의 차이

    print('#{} {}'.format(test_case, answer))
