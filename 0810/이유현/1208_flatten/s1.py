import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))
    cnt = 0
    while cnt <= dump:
        max_box = min_box = box_list[0]
        max_idx = min_idx = 0
        for box in box_list:
            if max_box < box:
                max_box = box
                max_idx = box_list.index(max_box)
            if min_box > box:
                min_box = box
                min_idx = box_list.index(min_box)
        if (max_box - min_box) == 0 or (max_box - min_box) == 1:
            break
        elif max_box - min_box > 1:
            box_list[max_idx] = max_box - 1
            box_list[min_idx] = min_box + 1
            cnt += 1

    print('#{} {}'.format(tc, max_box - min_box))

