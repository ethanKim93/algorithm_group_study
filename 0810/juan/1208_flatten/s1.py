import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    heights = [0] * 101
    max_height = 0
    min_height = 100
    for box in boxes:
        heights[box] += 1
        if max_height < box:
            max_height = box
        if min_height > box:
            min_height = box

    for i in range(dump):
        if max_height - min_height < 2:
            result = max_height - min_height
            break

        heights[max_height] -= 1
        heights[max_height-1] += 1
        heights[min_height] -= 1
        heights[min_height+1] += 1

        if not heights[max_height]:
            max_height -= 1
        if not heights[min_height]:
            min_height += 1

        result = max_height - min_height

    print('#{} {}'.format(tc, result))