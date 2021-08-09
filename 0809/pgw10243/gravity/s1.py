import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    width = int(input())
    heights = list(map(int,input().split()))
    falls = [] #각 층마다 최대 떨어지는 블록 개수를 모은 리스트
    for i in range(width):
        fall = 0
        for j in range(i+1,width): #시작한 층에서 아래층의 블록 수가 작으면 하나 떨어짐
            if heights[i] > heights[j]:
                fall += 1

        falls.append(fall)

    max_fall = 0
    for fall in falls:
        if max_fall < fall:
            max_fall = fall

    print('#{} {}'.format(tc,max_fall))
