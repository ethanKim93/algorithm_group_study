import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input()

    max_cnt = 0
    max_num = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if cards[i] == cards[j]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
            max_num = cards[i]
        elif max_cnt == cnt:
            if max_num < cards[i]:
                max_num = cards[i]
            else:
                pass
        else:
            pass

    print('#{} {}'.format(max_num, max_cnt))