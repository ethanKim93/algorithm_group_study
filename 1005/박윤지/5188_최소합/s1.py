import sys
sys.stdin = open('sample_input.txt', 'r')

# 좌, 우
dr = [0, 1]
dc = [1, 0]


def dfs(r, c, sumN):  # 행 위치, 열 위치, 지금까지 숫자의 합계
    global ans
    if r == N-1 and c == N-1:
        if ans > sumN + arr[r][c]:
            ans = sumN + arr[r][c]
        return
    if visited[r][c] == 0:
        visited[r][c] = 1
        sumN += arr[r][c]
        if sumN > ans:  # 중간에 끊어주지 않으면 시간 초과가 나서 ans를 계속 최솟값으로 갱신하고 그것보다 커지면 return 하도록 했다.
            return
        for i in range(2):
            ir = r + dr[i]
            ic = c + dc[i]
            if 0 <= ir < N and 0 <= ic < N and visited[ir][ic] != 1:
                dfs(ir, ic, sumN)
                visited[ir][ic] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 99999999999  # 충분히 커보이는 수로 설정
    visited = [[0]*N for _ in range(N)]
    dfs(0,0,0)
    print('#{} {}'.format(tc, ans))
