import sys
sys.stdin = open('sample_input.txt')

dy = [0, 1]  # 우, 하 방향으로만 진행
dx = [1, 0]


def load(score, row=0, col=0):
    global minimum
    if score > minimum:  # 백트래킹, 현재 점수가 최소점수보다 크다면 갈 필요 없음, 리턴
        return

    if row == N-1 and col == N-1:  # 마지막 지점 도착, 현재 점수가 최소보다 작다면 저장
        if score < minimum:
            minimum = score
        return

    for i in range(2):
        y = row + dy[i]
        x = col + dx[i]
        if 0 <= y < N and 0 <= x < N:  # field를 벗어나지 않을 경우
            load(score + field[y][x], y, x)  # 재귀


for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    minimum = 10 * N * N  # N by N이 들어오는데, 내부 최대값이 10이니까

    load(field[0][0])  # 시작 스코어 들고 함수로
    print("#{} {}".format(case + 1, minimum))