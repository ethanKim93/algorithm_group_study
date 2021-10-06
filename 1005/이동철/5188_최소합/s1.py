import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())

dr = [0, 1]
dc = [1, 0]


def dfs(row, col):
    global result, total

    if result < total:
        return

    if row == N - 1 and col == N - 1:
        result = total
        return

    for i in range(2):
        nr = row + dr[i]
        nc = col + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if (nr, nc) not in visited:
            visited.append((nr, nc))
            total += arr[nr][nc]
            dfs(nr, nc)
            total -= arr[nr][nc]
            visited.remove((nr, nc))
            #  tuple의 경우, 동일한 방식으로 복사할 경우
            #  서로 Identity가 같은 객체로 복사된다.
            # 즉, list처럼 새로운 메모리에 값을 할당하는 것이 아니라,
            # 복사된 변수가 원본과 같은 객체를 가리키고있다는 뜻이다.


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = []
    result = 3000
    total = arr[0][0]

    dfs(0, 0)

    print('#{} {}'.format(tc, result))


coordinate = [(0, 1), (1, 0)]


def BF(x, y, total):
    global result
    total += in_arr[x][y]
    # 우하단 끝에 도착했을 때
    if x == N - 1 and y == N - 1:
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
    in_arr = [list(map(int, input().split())) for _ in range(N)]
    # N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어지므로 처음 result값은 무조건 그 이상으로 설정한다.
    result = N ** 2 * 10
    BF(0, 0, 0)

    print('#{} {}'.format(tc, result))