# algorithm/1001/juan/ex2/s2.py
# 위에 베이비진 풀이 1. 기본 완전탐색  2. 재귀로 순열만들고 찾기
# 2번은 그날 했어서 1번으로 풀기

import sys
sys.stdin = open('sample_input.txt', 'r')

def babygin(arr):
    counter = [0 for _ in range(10)]  # 인덱스 숫자의 수를 저장
    for j in arr:
        counter[j] += 1
    
    for k in range(10):
        # triplet 검사
        if counter[k] >= 3:
            return 1  # babygin 맞음
        if k <= 7:
            if counter[k] and counter[k+1] and counter[k+2]:  # count 정렬 했으므로 인덱스 연속인 value들이 1, 1, 1로 존재하기만 하면 run
                return 1
    return 0  # babygin 아님


def order(player):
    for m in range(3, 7):
        if babygin(player[:m]):
            return m
    else:
        return 10  # 끝까지 봤더니 베이비진 없음


T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    c1 = []  # 플레이어1 카드
    c2 = []  # 플레이어2 카드
    for i in range(12):
        if not i % 2: # 짝수면
            c1.append(cards[i])
        else:
            c2.append(cards[i])

    # 카드 수가 3, 4, 5, 6 일 때 베이비진 찾기
    # 플레이어 1이 우선권을 갖는다. 끝까지 보기 전에 1이 먼저 babygin 맞추면 게임 끝

    ans = 0
    ans1 = order(c1)
    ans2 = order(c2)
    if ans1 == ans2 and ans1 != 10 and ans2 != 10:  # 이거 해야 정답 나옴
        ans = 1
    elif ans1 < ans2:
        ans = 1
    elif ans1 > ans2:
        ans = 2
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))
