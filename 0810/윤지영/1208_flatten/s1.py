import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    cnt = int(input())
    height = list(map(int,input().split()))
    idx_max = idx_min = 0
    h_max = h_min = height[0]
    for n in range(cnt+1):       # 최종적으로 최대,최소높이 구하기위해 인덱스 하나 추가
        for i in range(len(height)):
            if h_max < height[i]:
                h_max = height[i]
                idx_max = i
            if h_min > height[i]:
                h_min = height[i]
                idx_min = i
        if n <= cnt-1:         # 덤프 횟수가 끝나기 전까지는 덤프 반복(최종 높이 구하는 순회에선 제외하기 위해)
            height[idx_max] -= 1
            height[idx_min] += 1
            h_max = height[idx_max]
            h_min = height[idx_min]
        if height[idx_max]-height[idx_min] <= 1:
            break
    print('#{} {}'.format(tc, height[idx_max]-height[idx_min]))

