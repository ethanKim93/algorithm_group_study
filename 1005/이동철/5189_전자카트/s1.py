import sys
sys.stdin = open('sample_input.txt', 'r')


def office(idx, total):
    global value

    if 0 not in visited:    # 모든 곳 방문하고 최소 소비로 바꿔주기
        if value > total:
            value = total
        return
    elif value < total: # 방문 중인데 최소값 넘기면 리턴
        return

    for i in range(N):
        if i == idx or visited[i]:  # 현재 위치 혹은 이미 방문한 곳은 가지 않는다.
            continue
        elif i == 0 and 0 in visited[1:]:   # 아직 방문하지 않은 곳이 있으면 출발지로 가지 않는다.
            continue
        visited[i] = 1
        office(i, total + arr[idx][i])  # 재귀로 방문하면서 소비를 더하는 방식
        visited[i] = 0  # 방문하는 곳은 방문 처리해서 재방문 안하도록 하고, 방문이 끝나면 방문처리를 없애서 다른 경우도 계산하도록 한다.


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    value = 1000000
    office(0, 0)

    print('#{} {}'.format(tc, value))
