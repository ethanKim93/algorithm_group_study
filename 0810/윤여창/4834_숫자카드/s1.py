import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    cnt = [0] * 10
    for card in range(N):
        if cards[card]:
            cnt[cards[card]] += 1

    top_card_number = cnt[0]
    max_card = 0
    for k in range(1, len(cnt)):
        if top_card_number <= cnt[k]:
            top_card_number = cnt[k]
            max_card = k
    print('#{} {} {}'.format(tc, max_card, top_card_number))



# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
#
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

