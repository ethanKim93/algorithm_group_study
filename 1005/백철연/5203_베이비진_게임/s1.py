import sys
sys.stdin = open('sample_input.txt')

def win(cards_list, player):
    cnt = [0] * 12
    for j in cards_list:
        cnt[j] += 1

    for k in range(0, 10):
        if ((cnt[k] and cnt[k+1] and cnt[k+2] != 0) or (cnt[k] == 3)) and player == 1:
            return 1
        elif ((cnt[k] and cnt[k+1] and cnt[k+2] != 0) or (cnt[k] == 3)) and player == 2:
            return 2

    return

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int,input().split()))
    a = []
    b = []

    for i in range(len(cards)):
        if i % 2 == 0:
            a.append(cards[i])
            c = win(a, 1)
            if c == 1:
                print('#{} {}'.format(tc, c))
                break

        else:
            b.append(cards[i])
            d = win(b, 2)
            if d == 2:
                print('#{} {}'.format(tc, d))
                break

    if c is None and d is None:
        print('#{} {}'.format(tc, 0))





