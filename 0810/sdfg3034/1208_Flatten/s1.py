import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    for i in range(N):
        max_box = 0
        min_box = 100
        for box in boxes:
            if box > max_box:
                max_box = box
            if box < min_box:
                min_box = box
        boxes[boxes.index(max_box)] -= 1
        boxes[boxes.index(min_box)] += 1
    if max_box not in boxes:
        max_box -= 1
    if min_box not in boxes:
        min_box += 1

    print('#{}'.format(test_case),end=' ')
    print(max_box-min_box)