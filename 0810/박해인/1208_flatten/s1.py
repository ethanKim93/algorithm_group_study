import sys
sys.stdin = open("input.txt")

for test_case in range(1, 11):
    D = int(input()) # 덤핑 횟수
    boxes = list(map(int, input().split()))
    box_list = [0 for i in range(101)] # 0~100 높이의 box 리스트

    tallest = -1        # 최고값 초기화
    shortest = 101      # 최저값 초기화

    for i in range(100):
        box_list[boxes[i]] += 1  # box 높이를 box 높이별로 재정렬
        if boxes[i] > tallest:
            tallest = boxes[i]
        if boxes[i] < shortest:
            shortest = boxes[i]

    # 덤핑 횟수가 남아있거나, 평탄화 작업이 끝나지 않았을 때 반복
    # == 덤핑 횟수가 0이 되거나, tallest와 shortest의 차이가 1이 되면 종료
    while D > 0 and (tallest - shortest > 1):
        # 덤핑한 box 높이 조정
        box_list[tallest] -= 1
        box_list[tallest - 1] += 1
        box_list[shortest] -= 1
        box_list[shortest + 1] += 1

        # 해당 높이의 box가 없다면 칸 이동
        if box_list[shortest] == 0:
            shortest += 1
        if box_list[tallest] == 0:
            tallest -= 1

        D -= 1

    result = tallest - shortest
    print('#{} {}'.format(test_case, result))