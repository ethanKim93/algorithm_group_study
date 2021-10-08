import sys
sys.stdin = open('sample_input.txt')


def get_lowest_cost(idx, cost):  # idx 제품 숫자
    global min_cost
    # 2.
    if cost >= min_cost:  # 넘겨받은 비용이 min_cost를 초과한다면
        return  # 만들지 않고 그냥 돌아가기
    # 3.
    if idx == N:  # 하나씩 만들어서 만들어야 하는 제품을 모두 만들었다면
        min_cost = cost
        return
    # 1.
    for i in range(N):  # 열 검사
        if factory[i] == 0:  # 만약 i 공장에서 만든 적이 없다면
            factory[i] = 1  # 공장에서 만들었다!
            get_lowest_cost(idx+1, cost+costs[idx][i])  # 다음 제품을 검사하고, 우선 비용을 더해서 넘겨보기
            factory[i] = 0  # return되어 돌아왔다면 비용이 최소비용을 넘겼다는 뜻이니 방문했던 공장에서 만들지 않는걸로 처리


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    factory = [0]*N
    min_cost = 99999999
    get_lowest_cost(0, 0)

    print('#{} {}'.format(test_case, min_cost))