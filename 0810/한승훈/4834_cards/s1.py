import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    L = int(input())
    cards = list(map(int, list(input())))

    count_cards = [0] * 10 # 0~9의 숫자 카운트할 리스트 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for card in cards: # 숫자별 카드 삽입
        count_cards[card] += 1

    max_count = count_cards[0] # 카운트 초기값 설정
    max_num = 0
    for card_num in range(1,10): # 초기값을 제외한 1부터~9사이의 카드만 확인
        if count_cards[card_num] >= max_count: # >= : 같은 카운팅이여도 숫자가 큰것 도출
            max_count = count_cards[card_num]
            max_num = card_num
    print('#{} {} {}'.format(tc, max_num, max_count))
