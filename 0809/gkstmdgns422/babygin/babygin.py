import sys
sys.stdin = open('input.txt')

T = int(input())
# 3장의 카드가 연속적인 번호 = run
# 3장의 카드가 동일한 번호를 갖는 경우 triplet

for tc in range(1, T+1): # 테스트 케이스
    cards = input() # 0~9번의 6장 카드 모음
    count_cards = [0] * 10 # 카운트 행렬
    for card in cards:
        count_cards[int(card)] += 1

    triplet = 0
    run = 0
    idx = 0
    while idx < 10:
        if count_cards[idx] >= 6: # triplet이 2개인경우
            triplet += 2
            count_cards[idx] -= 6
        elif count_cards[idx] >= 3: # triplet이 1개인경우
            triplet += 1
            count_cards[idx] -= 3
        if count_cards[idx] == 2 and count_cards[idx+1] == 2 and count_cards[idx+2] == 2: # run이 2개인경우
            run += 2
            count_cards[idx] -= 2
            count_cards[idx + 1] -= 2
            count_cards[idx + 2] -= 2
        elif count_cards[idx] and count_cards[idx+1] and count_cards[idx+2]: # run이 1개인 경우
            run += 1
            count_cards[idx] -= 1
            count_cards[idx+1] -= 1
            count_cards[idx+2] -= 1
        idx += 1

    if triplet + run == 2:
        print('Baby-Gin')
    else:
        print('No Baby-Gin')






