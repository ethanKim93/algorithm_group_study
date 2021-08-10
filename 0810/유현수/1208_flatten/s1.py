import sys
sys.stdin=open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for i in range(dump):
        top_idx = 0
        for j in range(100):
            if boxes[top_idx] < boxes[j]:
                top_idx = j

        boxes[top_idx] -= 1

        bottom_idx = 0
        for j in range(100):
            if boxes[bottom_idx] > boxes[j]:
                bottom_idx = j

        boxes[bottom_idx] += 1

        if boxes[top_idx] - boxes[bottom_idx] <= 1:
            break

    top_idx = 0
    for j in range(100):
        if boxes[top_idx] < boxes[j]:
            top_idx = j

    bottom_idx = 0
    for j in range(100):
        if boxes[bottom_idx] > boxes[j]:
            bottom_idx = j

    print('#{} {}'.format(tc, boxes[top_idx] - boxes[bottom_idx]))