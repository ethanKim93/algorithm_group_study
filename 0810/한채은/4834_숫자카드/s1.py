import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input()))

    max_card = card_list[0]
    for m in card_list:
        if m > max_card:
            max_card = m

    count_list = [0] * 10
    for i in range(0, N):
        count_list[card_list[i]] += 1
        max_count = 0
        temp_card = 0

        for j in range(0, len(count_list)):
            if count_list[j] >= max_count:
                max_count = count_list[j]
                temp_card = j

    print('#{} {} {}'.format(test_case, temp_card, max_count))