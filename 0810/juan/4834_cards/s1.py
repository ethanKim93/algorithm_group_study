import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    card_count = int(input())
    cards = list(map(int, input()))
    counters = [0 for _ in range(10)]

    for card in cards:
        counters[card] += 1

    max_idx = idx = 0

    while idx < len(counters):
        if counters[idx] >= counters[max_idx]:
            max_idx = idx
        idx += 1

    print('#{} {} {}'.format(tc, max_idx, counters[max_idx]))