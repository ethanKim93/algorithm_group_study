import sys
sys.stdin =open('sample_input1.txt')

# 시너지 계산
def calc_syn(food):
    f1 = f2 = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if food[i] and food[j]:
                f1 += syn[i][j] + syn[j][i]
            if not food[i] and not food[j]:
                f2 += syn[i][j] + syn[j][i]
    return abs(f1-f2)

# 식재료 고르기 k = k번째 식재료, n = 지금까지 고른 식재료 수
def div_food(k, n):
    global min_diff
    if k >= N: return   # 식재료 다 본 경우 return

    if n == N//2:       # 지금까지 고른 식재료 수가 1/2이면 시너지 계산하고 최소값 갱신
        print(food)
        min_diff = min(min_diff, calc_syn(food))
        return

    # 선택지 2가지: k번째 재료 고르던가, 말던가
    for c in [1, 0]:
        food[k] = c
        div_food(k+1, n+c)
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    syn = []
    for _ in range(N):
        syn.append(list(map(int, input().split())))

    min_diff = 20000
    # 식재료 선택지 저장하는 빈 리스트
    food = [0]*N
    div_food(0, 0)

    print('#{} {}'.format(tc, min_diff))
