import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(1, T+1):
    N = int(input())
    ai = input()
    card_cnt = [0]*10
    for j in range(N):
        card_cnt[int(ai[j])] += 1

    max_num = -1
    for k in range(10):
        if card_cnt[k] >= max_num:
            result = k
            max_num = card_cnt[k]
    print('#{} {} {}'.format(case, result, card_cnt[result]))






