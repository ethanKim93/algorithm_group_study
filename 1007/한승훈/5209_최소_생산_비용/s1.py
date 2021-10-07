import sys
sys.stdin = open('sample_input.txt')


def back(idx, cost):
    global min_cost
    if min_cost < cost:  # 가지치기
        return
    if idx > N-1:
        min_cost = min(min_cost, cost)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            back(idx+1, cost+factory[idx][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_cost = 1500
    back(0,0)
    print('#{} {}'.format(tc, min_cost))