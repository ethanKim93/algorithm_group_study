# 기웅님 코드

import sys
sys.stdin = open('sample_input.txt')

def backtrack(current, cnt):
    global min_charge
    if cnt >= min_charge: return            # 최소 충전 횟수 넘으면 가지치기
    if current >= N-1:
        min_charge = min(min_charge, cnt)   # 최소 충전 횟수 갱신
    else:
        for b in range(1, batt[current]+1): # 배터리 교체 후 갈 수 있는 모든 경우의 수 탐색
            backtrack(current+b, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N, *batt = map(int, input().split())
    min_charge = N-2    # 최대 충전 N-2번
    backtrack(0, -1)    # 처음 충전 제외
    print('#{} {}'.format(tc, min_charge))