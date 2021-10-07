def min_cost(num, cost_sum):
    # num: 제품 번호, product_num: 제품 수, cost_sum: 비용 합계
    global min_val
    if num == N:                                        # 모든 배정이 끝난 경우
        if cost_sum < min_val:                          # (필요하다면) 최소 비용 갱신
            min_val = cost_sum
    elif cost_sum >= min_val:                           # 가지 치기 (제품이 남았지만 최소 비용을 초과하는 경우 제외)
        return
    else:
        for i in range(N):                              # 공장 후보 i
            if not check[i]:                            # 배정 안된 공장이면
                check[i] = 1                            # i공장은 배정 완료 처리
                # (다음제품 확인, 제품 수, 현재까지의 비용 + 다음 제품의 비용)
                min_cost(num+1, cost_sum+cost[num][i])  # n제품을 i공장에 배정한 비용 추가
                check[i] = 0                            # i 공장에 다른 제품을 배정하도록 준비(원상복구)


import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for i in range(N)]
    min_val =987654321
    check = [0 for i in range(N)]   # 공장 후보
    min_cost(0, 0)
    print('#{} {}'.format(tc, min_val))