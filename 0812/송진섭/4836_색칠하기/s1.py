import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sketchbook = [[0]*10 for _ in range(10)] # 0으로 색칠된 스케치북 생성
    purple = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1:  # 빨간색일 경우 1로 색칠
                   sketchbook[i][j] = 1
                elif color == 2:  # 파랑색일 경우 스케치북이 1로색칠된 경우 3으로 색칠하고 보라색 카운트
                    if sketchbook[i][j] == 1:
                        sketchbook[i][j] = 3
                        purple += 1
    print('#{} {}'.format(tc, purple))
