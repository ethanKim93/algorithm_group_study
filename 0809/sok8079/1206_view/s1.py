import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())    #테스트 케이스 길이
    heights = list(map(int, input().split())) #빌딩의 높이들
    cnt = 0 #조망권 확보수
    s_index = 2   #시작 위치

    while s_index < L - 2:  #마지막 오른쪽 2개는 0 0 이니까 확인 안 해도 됨
        if heights[s_index] <= heights[s_index-2] or heights[s_index] <= heights[s_index-1] or heights[s_index] <= heights[s_index+1]:  #왼쪽에 있는 것들보다 작으면 s_index 한 칸 이동, 한 칸 오른쪽 옆에 있는 빌딩보다 작으면 한 칸 이동
            s_index += 1
            pass

        elif heights[s_index] <= heights[s_index+2]:    #두 칸 오른쪽 옆에 있는 빌딩보다 작으면 두 칸 이동
            s_index += 2
            pass

        else:   #조망권이 확보 된 경우
            max_height_index = heights[s_index - 2]
            if heights[s_index - 1] > max_height_index:
                max_height_index = heights[s_index - 1]
            if heights[s_index - 2] > max_height_index:
                max_height_index = heights[s_index - 2]
            if heights[s_index + 1] > max_height_index:
                max_height_index = heights[s_index + 1]
            if heights[s_index + 2] > max_height_index:
                max_height_index = heights[s_index + 2]

            cnt += heights[s_index] -max_height_index   #조망권 확보 숫자 더하기
            s_index += 3    #오른쪽으로 3칸 이동
    print('#{} {}'.format(tc, cnt))