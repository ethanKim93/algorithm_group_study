# 삽질하다가 설명 참고해서 풂.... dfs 비슷하게 된듯

import sys
sys.stdin = open('sample_input.txt', 'r')

def calc(a):  # 충전한 곳
    global ans, cnt
    bus = batt[a]
    cnt += 1  # 맨 처음 충전한 거는 카운트로 안치는데, 귀찮아서 추가하고 마지막 print에서 -1해줬다
    if ans < cnt:
        return
    if a + bus >= N:
        if ans > cnt:
            ans = cnt
        return
    else:
        for i in range(bus, 0, -1):
            calc(a+i)
            cnt -= 1  # 끝까지 가거나 실패해서 돌아온거니까 카운트 했던 걸 취소해줘야함


T = int(input())

for tc in range(1, T+1):
    batt = list(map(int, input().split()))
    N = batt[0]
    ans = 9999
    cnt = 0
    calc(1)
    print('#{} {}'.format(tc, ans-1))



    # def powerset(arr, k):
    #     c = [1, 0]
    #     if 0 <= k < len(arr):
    #         for i in range(2):
    #             arr[]


    # for i in range(1 << (N-2)):
    #     for j in range(N-2):
    #         if i & (1 << j):


    # bus = temp[0]  # 첫번째 정류장에서 버스가 가진 배터리
    # powerset(temp[1:])  # 첫번째 정류장 빼고 시작