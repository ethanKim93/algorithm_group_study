import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)] # 10*10 빈배열
    result = 0 # 보라색 갯수를 담을 result
    for i in range(N):
        area = list(map(int, input().split()))
        x = [area[0], area[2]]      # x축 점 두개
        y = [area[1], area[3]]      # y축 점 두개

        for j in range(x[0], x[1]+1):    # x축 점 두개 사이 반복
            for k in range(y[0], y[1]+1):# y축 점 두개 사이 반복
                if not arr[j][k]:        # 안의 값이 0이 아니라면
                    arr[j][k] = area[4]  # 1,2 둘중 하나 대입
                else:
                    arr[j][k] = 3

    for l in range(10):         # 이중배열내에서 보라색값 구하기
        for m in range(10):
            if arr[l][m] == 3:
                result += 1
    print('#{} {}'.format(tc, result))