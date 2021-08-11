import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))

    max_num = -1
    max_cnt = 0
    for card in range(0, 10):
        if cards.count(card) >= max_cnt:
            max_cnt = cards.count(card)
            max_num = card

    print('#{} {} {}'.format(tc, max_num, max_cnt))


