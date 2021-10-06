import sys
sys.stdin = open('sample_input.txt')


def recursion(idx, total):
    global mini

    # 백트래킹으로 소비량이 최솟값을 넘어간 경우 return
    if total > mini:
        return

    # 모든 곳을 방문한 경우 (출발지로 돌아온 경우)
    if 0 not in visited:
        # 최소 소비량 갱신
        if total < mini:
            mini = total
        return

    # 방문할 곳 돌면서
    for i in range(N):
        # 현재위치에 있으면 방문 X
        if i == idx:
            continue
        # 이미 방문한 곳은 방문 X
        if visited[i]:
            continue

        # 아직 방문 하지 않은 곳이 있으면 출발지로 안가고
        if i == 0 and 0 in visited[1:]:
            continue

        # 방문 표시
        visited[i] = 1
        # 재귀를 탐
        recursion(i, total + arr[idx][i])
        # 방문 표시 0으로 만들어주기
        visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문 체크
    visited = [0] * N

    # 임의의 큰 수
    mini = N * N * 100

    # 시작점 들고 함수로 감
    recursion(0, 0)

    print('#{} {}'.format(tc, mini))