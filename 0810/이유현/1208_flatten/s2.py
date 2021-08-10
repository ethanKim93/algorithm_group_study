
dump = 834
box_list = [42, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83, 22, 17, 19, 96, 48, 27, 72, 39, 70, 13, 68, 100, 36, 95, 4, 12, 23, 34, 74, 65, 42, 12, 54, 69, 48, 45, 63, 58, 38, 60, 24, 42, 30, 79, 17, 36, 91, 43, 89, 7, 41, 43, 65, 49, 47, 6, 91, 30, 71, 51, 7, 2, 94, 49, 30, 24, 85, 55, 57, 41, 67, 77, 32, 9, 45, 40, 27, 24, 38, 39, 19, 83, 30, 42]
cnt = 0
while cnt <= 2:
    max_box = min_box = box_list[0]
    max_idx = min_idx = 0
    for box in box_list:
        if max_box < box:
            max_box = box
            max_idx = box_list.index(max_box)
        if min_box > box:
            min_box = box
            min_idx = box_list.index(min_box)
    print(max_box, max_idx, min_box, min_idx)
    if (max_box - min_box) == 0 or (max_box - min_box) == 1:
        break
    elif max_box - min_box > 1:
        box_list[max_idx] = max_box - 1
        box_list[min_idx] = min_box + 1
        cnt += 1

# print('#{} {}'.format(tc, cnt))