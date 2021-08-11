import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split())) # 박스 리스트
    max_h = min_h = box[0] # 높이 초기값
    while dump > 0: # dump가 0이 될때까지 진행
        for idx in range(len(box)): # max,min값 구하기
            if box[idx] > max_h:
                max_h = box[idx]
                max_idx = idx
            if box[idx] < min_h:
                min_h = box[idx]
                min_idx = idx
        box[max_idx] -= 1 # max는 -1 min은 +1
        box[min_idx] += 1
        dump -= 1
        max_h -= 1
        min_h += 1

    for idx in range(len(box)):
        if box[idx] > max_h:
            max_h = box[idx]
        if box[idx] < min_h:
            min_h = box[idx]
    print('#{} {}'.format(tc, max_h-min_h))


