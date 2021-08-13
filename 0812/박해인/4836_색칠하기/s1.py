import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 칠할 영역의 개수
    red = list()    # 빨간색으로 칠한 좌표
    blue = list()   # 파란색으로 칠한 좌표
    count = 0       # 보라색이 된다면 count 해줄 변수 선언

    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2+1):           # 끝까지 돌아야하니까 x2+1
            for y in range(y1, y2+1):
                if color == 1:          # 빨간색이면
                    red.append((x, y))          # red list에 담아주기
                else:                   # 파란색이면
                    blue.append((x, y))         # blue list에 담아주기

    # print(blue)
    # print(red)
    # purple = set(red) & set(blue)
    # print(purple)
    # 내장함수 쓰면 안됨........................
    for i in range(len(red)):
        for j in range(len(blue)):
            if red[i][0] == blue[j][0] and red[i][1] == blue[j][1]:     # if red list와 blue list 중복되는 요소가 있다면
                count += 1

    print('#{} {}'.format(test_case, count))
