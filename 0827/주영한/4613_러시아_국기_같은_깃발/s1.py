import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 최댓값으로 설정하여 업데이트 할 수 있게 한다.
    cnt = N * M
    flags = [list(input()) for _ in range(N)]
    middle_inform = []
    for row in range(N):
        white_row = blue_row = red_row = M
        for col in range(M):
            if flags[row][col] == "W":
                white_row -= 1
            if flags[row][col] == "B":
                blue_row -= 1
            if flags[row][col] == "R":
                red_row -= 1
        middle_inform.append([white_row, blue_row, red_row])

    # middle_inform에 대해 구분선을 어디 둘지 결정하고 그 경우에 대해 temp_cnt를
    # 확인하고, cnt와 비교하여 업데이트 한다.
    for i in range(1, N - 1):   # 구분선이 들어갈 수 있는 곳 1 ~ N - 2 / 2 ~ N - 1
        for j in range(i + 1, N):
            temp_cnt = 0
            for white in range(0, i):
                temp_cnt += middle_inform[white][0]
            for blue in range(i, j):
                temp_cnt += middle_inform[blue][1]
            for red in range(j, N):
                temp_cnt += middle_inform[red][2]
            if temp_cnt < cnt:
                cnt = temp_cnt
    print("#{} {}".format(tc, cnt))