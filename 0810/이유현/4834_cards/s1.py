import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for i in range(1, t+1):
    n = int(input())
    card_list = list(map(int, input()))

    cnt = [0] * 10
    for i in range(n):
        if card_list[i]:
            cnt[card_list[i]] += 1

    max_idx = 0
    max_card = 0
    for idx in range(len(cnt)):
        if max_idx <= cnt[idx]:
            max_idx = cnt[idx]
            max_card = idx

    print('#{} {} {}'.format(i, max_card, max_idx))

