import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    mid = N // 2 # 가운데 좌표
    R = mid
    L = mid
    result = 0

    for i in range(N):
        for j in range(L, R + 1): # range 범위를 조절하는 식으로, 5x5 행렬이라면
            result += arr[i][j]   #j의 범위는 #0 range(2, 3)
        if i < mid:
            L -= 1
            R += 1                #1 range(1, 4)  #2 range(0, 5)
        elif i >= mid:
            L += 1                #3 range(1, 4) #4 range(2, 3)
            R -= 1
    print('#{} {}'.format(tc,result))



