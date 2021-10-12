import sys
sys.stdin = open('sample_input.txt')

def search(station):
    global min_change, change

    if change >= min_change:         # 최소 교체 횟수보다 많이 교체하면 종료
        return

    if station >= len(batteries):    # 목적지 도착시(목적지 이상 거리 운행 가능할 때)
        if min_change > change:      # 최소값 갱신
            min_change = change
        return

    for i in range(station+batteries[station], station, -1):   # 최대가능한 정류장부터 현재 정류장까지 탐색
        change += 1                  # 탐색 전 교체
        search(i)                    # 탐색
        change -= 1

for tc in range(1, int(input())+1):
    temp = list(map(int, input().split()))
    N, batteries = temp[0], temp[1:]             # N : 정류장수, batteries: 1~N-1까지 정류장에서의 배터리 용량
    min_change = N                   # 정류장 수 이상으로 교체가 불가능하기 때문에 N으로 최댓값 초기화
    change = 0
    search(0)                        # 첫번째 정류장부터 탐색
    print('#{} {}'.format(tc, min_change-1))     # 첫번째 충전은 교체횟수에 포함 안되기 때문에 1을 빼면 최소값


# DP
# for test in range(1, int(input()) + 1):
#     N, *battery = map(int, input().split())
#     dp = [float('inf')] * N
#     dp[N - 1] = 0
#     for i in range(N - 1, -1, -1):
#         for j in range(i - 1, -1, -1):
#             if j + battery[j] >= i:
#                 dp[j] = min(dp[j], dp[i] + 1)
#     print('#{} {}'.format(test, dp[0]-1))