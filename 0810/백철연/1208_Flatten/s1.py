import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    for i in range(N):
        max_box = 0
        min_box = 100
        for box in boxes:         # 리스트에서 하나씩 꺼냄
            if box > max_box:     # 가장 높은 박스를
                max_box = box     # max 박스에 할당
            if box < min_box:    # min도
                min_box = box
        boxes[boxes.index(max_box)] -= 1 # 최고 높은 박스의 인덱스 찾아서 1씩 감소
        boxes[boxes.index(min_box)] += 1 # 최고 낮은 박스의 인덱스 찾아서 1씩 증가
    if max_box not in boxes:
        max_box -= 1                  # 
    if min_box not in boxes:
        min_box += 1                #

    print('#{} {}'.format(test_case,max_box-min_box))

#




