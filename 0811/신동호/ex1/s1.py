import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box = [0] * N # 기존 박스
    new_box = [[0] * N for _ in range(N)] # 차이값 저장할 새로운 박스
    for i in range(N):
        box[i] = list(map(int,input().split()))
    for j in range(N):
        for i in range(N): # 모든 요소에 대해 상하좌우가 유효한 값인지 검사
            if 0 <= i-1:
                new_box[i][j] += abs(box[i][j] - box[i-1][j])
            if 0 <= j-1:
                new_box[i][j] += abs(box[i][j] - box[i][j-1])
            if N > i+1:
                new_box[i][j] += abs(box[i][j] - box[i+1][j])
            if N > j+1:
                new_box[i][j] += abs(box[i][j] - box[i][j+1])
    # print(box)
    # print(new_box)
    print('#{} {}'.format(tc,sum(sum(new_box,[]))))

