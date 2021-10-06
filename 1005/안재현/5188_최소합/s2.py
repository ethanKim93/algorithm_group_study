import sys
sys.stdin = open('sample_input.txt')


coordinate = [(0, 1), (1, 0)]


def BF(x, y, total):
    global result
    total += arr[x][y]
    # 우하단 끝에 도착했을 때
    if x == N-1 and y == N-1:
        if result > total:
            result = total
    # 시간초과를 막기 위해서 끝에 도달하기도 전에 총합이 결과값보다 커질 경우엔 해당 함수 종료
    elif result < total:
        return

    # 우측/하단 2방향만 탐색
    for i in coordinate:
        # i = (1, 0) 일때 dx = 1, dy = 0
        dx, dy = i
        nx, ny = x + dx, y + dy
        if nx < N and ny < N:
            BF(nx, ny, total)


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어지므로 처음 result값은 무조건 그 이상으로 설정한다. (실제 최대값은 아님)
    result = N**2*10
    BF(0, 0, 0)

    print('#{} {}'.format(tc, result))