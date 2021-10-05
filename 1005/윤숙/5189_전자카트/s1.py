import sys

sys.stdin = open('input.txt', 'r')


def Min_consumption(c, s, total):
    global minV
    #사무실에 돌아와야하므로
    if c == N - 1: # 더한 횟수를 카운트해서 N번 합하면, 0번 인덱스의 값을 더해준다.
        total += road[s][0]
        if minV > total:
            minV = total
            return
    # 최소값보다 커지면 바로 커트
    if total > minV:
        return

    for j in range(1, N):
        if s == j:
            continue
        if not visited[j]:
            visited[j] = 1
            Min_consumption(c + 1, j, total + road[s][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minV = 9999999999
    total = 0
    Min_consumption(0, 0, 0)
    print('#{} {}'.format(tc, minV))
