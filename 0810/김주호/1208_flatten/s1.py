import sys
sys.stdin = open("input.txt")

for case in range(10):
    move = int(input())

    boxes = list(map(int, input().split()))

    for mov in range(move):
        max_height = max(boxes)
        min_height = min(boxes)

        boxes[boxes.index((max_height))] -= 1
        boxes[boxes.index((min_height))] += 1

        if max_height - min_height <= 1:
            break

    max_height = max(boxes)
    min_height = min(boxes)

    print("#{} {}".format(case + 1, max_height - min_height))
