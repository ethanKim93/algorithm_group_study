import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10*N**2

    def DFS(r, c, dist):                        # 현재 위치 (행/열) / dist: 누적 거리
        global ans
        if dist >= ans: return                  # 만약 지금 계산 중인 거리(dist)가 전역에 있는 최솟값(ans)보다 크거나 같으면 가지치기
        if r == c == N-1:                       # 도착지점에 도착한 경우
            ans = min(ans, dist)                # ans에 지금까지 최소거리 저장
        else:                                   # 도착하지 않았다면
            if r+1 < N:                         # 아래로 이동 했을 때 범위를 벗어나지 않으면
                DFS(r+1, c, dist+arr[r+1][c])   # 아래로 이동
            if c+1 < N:                         # 오른쪽으로 이동 했을 때 범위를 벗어나지 않으면
                DFS(r, c+1, dist+arr[r][c+1])   # 오른쪽으로 이동

    DFS(0, 0, arr[0][0])                        # 0, 0에서 시작 / 시작값은 ans[0][0]
    print('#{} {}'.format(tc, ans))