import sys
sys.stdin = open('input.txt')

for T in range(1,11):
    dump = int(input()) #덤프 횟수
    height = list(map(int,input().split())) #박스 높이

    idx_max = 0
    idx_min = 0

    for i in range(dump):
        Min, Max = 99999999999999, -1
        for j in range(0, 100):
            if height[j] < Min:
                Min = height[j]
                idx_min = height.index(Min)
            if height[j] > Max:
                Max = height[j]
                idx_max = height.index(Max)

        if height[idx_max] - height[idx_min] > 1:
            height[idx_max] = Max-1
            height[idx_min] = Min+1

    print('#{} {}'.format(T, max(height) - min(height)))
