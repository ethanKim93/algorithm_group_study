import sys
sys.stdin =open('input.txt')

T = int(input())

for tc in range(1,T+1):
    width = int(input())
    heights = list(map(int,input().split()))

    #가장 높은 길이 구하기
    max_h = heights[0]
    for i in heights:
        if max_h < i:
            max_h = i

    max_list = [0] * len(heights)

    for idx,height in enumerate(heights):

        dif_list = [0]*max_h #배열 크기 지정, 0으로 초기화
        for i in range(0,height):
            dif_list[i] = len(heights)-(idx+1) #해당 길이 만큼 낙차 최대값으로 초기화

        for j in range(idx+1,len(heights)):
            for k in range(0,heights[j]):
                dif_list[k] -= 1

        max_dif = dif_list[0]
        for i in dif_list:
            if max_dif < i:
                max_dif = i

        max_list[idx] = max_dif

    result = max_list[0]
    for i in max_list:
        if result < i:
            result = i

    print(result)


