import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump_times = int(input())
    boxes = list(map(int, input().split()))
    # 박스 높이의 분포를 카운팅하고, 이때 가장 높은 높이와 가장 낮은 높이를 찾는다.
    heights_num = [0] * 101
    max_height = 0
    min_height = 100
    for box in boxes:
        heights_num[box] += 1
        if max_height < box:
            max_height = box
        if min_height > box:
            min_height = box

    # 덤프를 실시한다. 가장 높은 높이와 가장 낮은 높이의 카운팅을 하나 차감해주고,
    # 가장 낮은 높이보다 하나 큰 높이와 가장 높은 높이보다  하나 작은 높이의 카운팅을 하나 높인다.
    for dump in range(dump_times):

        # 더이상 덤프를 못하는 경우 break문으로 빠져 나와준다.
        if max_height - min_height < 2:
            result = max_height - min_height
            break

        heights_num[max_height] -= 1
        heights_num[max_height - 1] += 1
        heights_num[min_height] -= 1
        heights_num[min_height + 1] += 1

        # 가장 높은 높이와 가장 낮은 높이를 업데이트 한다
        if not heights_num[max_height]:
            max_height -= 1
        if not heights_num[min_height]:
            min_height += 1

        result = max_height - min_height

    print("#{} {}".format(tc, result))
