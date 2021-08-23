import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]   #2d 행렬로 입력받음
    ans = 0
    for i in range(N):
        for j in range(N):
            if i < N//2:                                # i 가 중간보다 작은 경우
                if N//2 -i <= j <= N//2 +i:             # 중간에서 i를 빼고 더하고 범위까지 더함
                    ans += arr[i][j]
            else:                                       # i 가 중간보다 큰 경우
                if N//2 -(N-1-i) <= j <= N//2 + (N-1-i): # N-1-i를 뺴고 더하고 범위까지 더함
                    ans += arr[i][j]

    print('#{} {}'.format(tc, ans))
