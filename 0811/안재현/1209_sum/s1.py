import sys

sys.stdin = open('input.txt')

for _ in range(0, 10):
    T = int(input())
    arr = []
    high = 0
    for i in range(100):
        arr.append(list(map(int, input().split())))

    for i in range(100):
        sum_list = [0, 0, 0, 0]
        for j in range(100):
            sum_list[0] += arr[i][j]    # 행 값 더하기
            sum_list[1] += arr[j][i]    # 열 값 더하기
            sum_list[2] += arr[j][j]    # 좌상단에서 우하단으로 대각선값 더하기
            sum_list[3] += arr[100 - j - 1][100 - j - 1]    # 우상단에서 좌하단으로 대각선값 더하기
        for a in sum_list:
            if high < a:
                high = a
    print('#{} {}'.format(T, high))