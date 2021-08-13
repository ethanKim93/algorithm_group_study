import sys
sys.stdin = open('sample_input.txt')

test_cases = int(input())
for test in range(test_cases):
    red_list = []
    blue_list = []

    box_cnt = int(input())
    for box in range(box_cnt):
        a, b, c, d, e = map(int, input().split())

        if e == 1: # 빨간색 칠할 상자
            for x in range(c, a-1, -1):
                for y in range(d, b-1, -1):
                    red_list.append((x,y))
        else:
            e == 2 # 파란색 칠할 상자
            for x in range(c, a-1, -1):
                for y in range(d, b-1, -1):
                    blue_list.append((x,y))

    purple_box = 0
    for color in blue_list: # 파란색 상자 속에 있는 튜플이 빨간색 상자 안에 있는 개수를 셈
        if color in red_list:
            purple_box += 1
    print('#{} {}'.format(test+1, purple_box))