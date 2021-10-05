import sys
sys.stdin = open('sample_input.txt')

def get_minimum(idx, total):
    global value

    if 0 not in visited:  # 모든 곳 방문하고 최소 소비로 바꿔주기
        if value > total:
            value = total
        elif value < total:
            return

        for i in range(N):
            if i == idx or visited[i]:  # 현재 위치이거나 이미 방문했던 곳은 가지 않는다.
                continue
            elif i == 0 and 0 in visited[1:]:  # 아직 방문하지 않은 곳이 있다면 출발지로 가지 않는다
                continue
            visited[i] = 1  # 방문하기
            get_minimum(i, total+data[idx][i])  # cost 더하기
            visited[i] = 0  # 방문 취소하기


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    value = 1000000
    get_minimum(1, 0)
    print('#{} {}'.format(test_case, ans))