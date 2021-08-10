import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = list(map(int,input().split()))
    boxes = [0] * N #상자 빈 배열 생성
    for i in range(Q):
        L, R = list(map(int, input().split()))
        for ind in range(L, R+1):
            boxes[ind-1] = i+1 #상자에 시행
    print('#{} '.format(tc), end='')
    print(*boxes)