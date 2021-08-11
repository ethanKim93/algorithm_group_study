import sys
sys.stdin = open('input.txt')

Test_Cases = int(input())
for test_case in range(Test_Cases):
    array_cnt = int(input())

    arr = []
    for _ in range(array_cnt):
        arr.append(list(map(int, input().split())))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0] # 상 우 하 좌


    result_sum = 0
    for x in range(array_cnt): # 행 배열 순회할 x
        for y in range(array_cnt): # 열 배열 순회할 y => arr[x][y] x행 y열
            for i in range(4):
                test_x = x + dx[i]
                test_y = y + dy[i]
                if 0 <= test_x < 5 and 0 <= test_y < 5:
                    result_sum += abs(arr[test_x][test_y]-arr[x][y])

    print(result_sum)
