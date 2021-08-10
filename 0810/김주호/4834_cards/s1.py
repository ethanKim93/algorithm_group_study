import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for case in range(T):
    N = int(input())
    cards = input()

    card_num_check = {}

    for card in cards:
        try:
            card_num_check[card] += 1
        except:
            card_num_check[card] = 1

    card_max_key = card_max_num = 0
    for card_key, card_num in card_num_check.items():
        if card_max_num < card_num:
            card_max_num = card_num
            card_max_key = card_key
        elif card_max_num == card_num:
            if card_max_key < card_key:
                card_max_key = card_key

    print("#{} {} {}".format(case + 1, card_max_key, card_max_num))
