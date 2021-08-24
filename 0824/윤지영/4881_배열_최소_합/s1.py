import sys
sys.stdin = open("sample_input.txt")

def board_sum(i):
    global N, board_min, result
    if board_min < result:
        return              # 가지치기, 덧셈중인 result가 이미 최소값을 넘으면 볼 필요가 없으므로
    if i == N:
        if board_min > result:      # 행 i가 N이 된다는 것은, N-1번째 마지막행까지 모두 순회한것이므로 그때까지의 result값을 비교하여 최소값 갱신
            board_min = result
            return
    for j in range(N):
        if visited[j] == 0:
            result += boards[i][j]
            visited[j] = 1
            board_sum(i+1)
            result -= boards[i][j]
            visited[j] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    boards = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    board_min = N * 9
    result = 0
    board_sum(0)
    print('#{} {}'.format(tc, board_min))


