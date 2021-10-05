import sys
sys.stdin = open('sample_input.txt')

def backtrack(i, s):
    global min_sum
    if visited.count(1) == N-1:         # 시작점 빼고 다 방문했을 때
        if s+arr[i][0] < min_sum:       # 최소값 갱신
            min_sum = s+arr[i][0]

    for k in range(1, N):               # 0번 제외 모든 곳 순회
        if not visited[k] and i!=k:     # 미방문했고, 현재 위치와 다른 곳을 가도록
            visited[k] = 1
            backtrack(k,s+arr[i][k])
            visited[k] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N     # 방문 배열 정의
    min_sum = 100*N     # 최대 100이하의 자연수*N 경로로 초기화
    backtrack(0,0)      # 0번 인덱스부터 시작
    print('#{} {}'.format(tc, min_sum))