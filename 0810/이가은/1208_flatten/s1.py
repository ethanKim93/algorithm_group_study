import sys
sys.stdin = open('input.txt')

for test_case in range(10):
    dump_cnt = int(input())
    boxes_height = list(map(int, input().split()))

    while dump_cnt >0:
        max_box = max(boxes_height)
        min_box = min(boxes_height)
        boxes_height[boxes_height.index(max_box)] -= 1
        boxes_height[boxes_height.index(min_box)] += 1
        dump_cnt -= 1

    print('#{} {}'.format(test_case+1, max(boxes_height)-min(boxes_height)))