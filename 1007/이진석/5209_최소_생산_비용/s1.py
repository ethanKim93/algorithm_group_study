import sys
sys.stdin = open('sample_input.txt')

def calc(product, cost):
    global min_cost
    if min_cost <= cost:            # 최소값보다 현재 비용이 크면 종료
        return

    if product == N:                # 모든 제품비용을 계산했을 때 최소값 갱신
        min_cost = cost
        return

    for i in range(N):
        if not factory[i]:          # 제품을 담당하고있지 않은 공장일 때
            factory[i] = 1
            calc(product+1, cost + V[product][i])   # 다음번호의 제품 단가 계산
            factory[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())                # 제품 갯수
    V = [list(map(int, input().split())) for _ in range(N)]     # 각 공장별 단가(0번부터시작)
    min_cost = 15*99    # 최대값으로 초기화
    factory = [0] * N   # 각 공장별 제품 담당 여부
    calc(0, 0)
    print('#{} {}'.format(tc, min_cost))