import sys
sys.stdin = open('sample_input.txt')

# 우, 하 방향
dy = [0, 1]
dx = [1, 0]

# 재귀를 돌면서 내가 몇 점을 들고 있는지 확인
def load(score, row=0, col=0):
    global minimum
    # 백트래킹으로 현재 점수가 최소 점수보다 크면 return
    if score > minimum:
        return

    # row랑 col이 N-1이 되면 마지막 지점 도착
    if row == N-1 and col == N-1:
        # 현재 점수가 최소보다 작다면 저장
        if score < minimum:
            minimum = score
        return

    # 우, 하 로만 진행
    for i in range(2):
        # 그 방향대로 진행
        y = row + dy[i]
        x = col + dx[i]
        # field를 벗어나지 않을 경우 (범위 설정)
        if 0 <= y < N and 0 <= x < N:
            load(score + field[y][x], y, x) # 재귀를 탐


for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    # N by N이 들어오는데 내부 최대값이 10이니까
    minimum = 10 * N * N

    # 시작 스코어 들고 함수로 감
    load(field[0][0])
    print("#{} {}".format(case + 1, minimum))