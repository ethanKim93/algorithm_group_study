import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1): # 테스트 케이스
    width = int(input()) # 총 길이
    heights = list(map(int, input().split())) # 상자들
    ans = [] # 낙차들의 리스트

    i = 0
    ans_num = 0 # 초기 낙차
    while i < width:
        ans_num = 0
        for j in range(i+1, width):
            if heights[i] > heights[j]:
                ans_num += 1
        i += 1
        ans.append(ans_num)

    max_ans = 0
    for num in ans:
        if num > max_ans:
            max_ans = num
    print(max_ans)



