import sys
sys.stdin = open('sample_input.txt')

di, dj = [1, 0], [0, 1]         # 아래쪽, 위쪽 방향
def backtrack(i, j, s):
    global min_sum
    if s >= min_sum:            # 가다가 최소합보다 크거나 같으면 return
        return
    if (i,j) == (N-1, N-1):     # 마지막 지점 도착시 최소값 갱신
        if s < min_sum:
            min_sum = s
    for k in range(2):          
        ni, nj = i+di[k], j+dj[k]
        if ni < N and nj < N and not visited[ni][nj]:
            visited[ni][nj] = 1
            backtrack(ni, nj, s+arr[ni][nj])
            visited[ni][nj] = 0
    
    

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    min_sum = N*13*2            # N <= 13 이므로 대강 최대크기로 초기화
    backtrack(0,0,arr[0][0])    # 시작점 0,0, 첫 합으로 초기화
    print('#{} {}'.format(tc, min_sum))