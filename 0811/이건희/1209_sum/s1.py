import sys
sys.stdin = open("input.txt")

for tc in range(10):
    tc_num = int(input())
    maps = [list(map(int,input().split())) for _ in range(100)]
    preans = [] # row_sum + col_sum
    ans = 0
    right_sum = left_sum = 0 # 대각선 오른쪽 방향, 왼쪽 방향

    for r in range(100):
        row_sum = 0 # 행이 바뀔 때 마다 초기화
        for c in range(100):
            row_sum += maps[r][c]
            if r == c: # 오른쪽 방향 대각선
                right_sum += maps[r][c]
        preans.append(row_sum)

    cnt = 0
    for c in range(100):
        col_sum = 0
        for r in range(100):
            col_sum += maps[r][c]  # 열이 바뀔 때 마다 초기화
            if r + c == 99:
                cnt +=1
                left_sum += maps[r][c] # 왼쪽 방향 대각선
        preans.append(col_sum)

    # Find max value
    for i in preans:
        if ans < i:
            ans = i

    if ans < right_sum:
        ans = right_sum

    if ans < left_sum:
        ans = left_sum



    print("#{} {}".format(tc_num, ans))