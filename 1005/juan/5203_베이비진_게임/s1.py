def baby_gin():
    # 0  ~ 9 사이의 카드
    card1 = [0 for _ in range(10)]
    card2 = [0 for _ in range(10)]

    """
    run -> 연속된 숫자 3개 이상
    triplet -> 같은 숫자 3개 이상
    """
    for idx in range(12):
        n = cards[idx]
        if not idx % 2:                 # 짝수 -> player1
            card1[n] += 1               # idx 하나 증가시키고
            if card1[n] == 3:           # triplet이면 -> player1 승리
                return 1
            if check_run(card1) == 1:   # run이면 -> player1 승리
                return 1
        else:                           # 홀수 -> player2
            card2[n] += 1
            if card2[n] == 3:           # triplet이면 -> player2 승리
                return 2
            if check_run(card2) == 1:   # run이면 -> player2 승리
                return 2
    return 0                            # return 안만났다면 12개의 카드를 도는 동안 승부 x -> 무승부

def check_run(card):
    # 0 ~ 9까지의 숫자 카드 중에서
    for i in range(8):                  # 최대 i + 2 -> 9 (마지막 인덱스 9)
        if card[i] >= 1 and card[i+1] >= 1 and card[i+2] >= 1:  # 연속된 수가 1이상 체크되어있다면 run
            return 1

import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))  # 12장의 카드 정보
    winner = baby_gin()
    print('#{} {}'.format(tc, winner))