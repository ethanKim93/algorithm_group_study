import sys

sys.stdin = open('sample_input.txt')


def backtrack(k, cost):
    global min_cost
    if cost >= min_cost: return  # 비용이 최소비용 이상이면 가지치기
    if k == N:  # 최소비용 갱신
        min_cost = min(cost, min_cost)
    else:
        for w in range(N):  # 갈수 있는 곳 0~N-1
            if not visited[w]:  # 미방문한 곳이면
                visited[w] = 1  # 방문 처리
                backtrack(k + 1, cost + V[k][w])  # 코스트 계산하고
                visited[w] = 0  # 돌아오면 미방문 처리


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    # 선택할 수 있는 열의 가지 수 Ex. N=3 -> 0, 1, 2
    visited = [0] * N
    min_cost = 99 * N
    backtrack(0, 0)
    print('#{} {}'.format(tc, min_cost))