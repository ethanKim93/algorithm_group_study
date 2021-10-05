import sys
sys.stdin = open('sample_input.txt')


def check_babygin(num_list):
    count = [0] * 12
    for i in num_list:
        count[i] += 1
    tri = run = 0
    idx = 0

    while idx < 10:
        if count[idx] >= 3:
            count[idx] -= 3
            tri += 1
            continue
        if count[idx] >= 1 and count[idx+1] >= 1 and count[idx+2] >= 1:
            count[idx] -= 1
            count[idx+1] -= 1
            count[idx+2] -= 1
            run += 1
            continue
        idx += 1
    return 1 if tri or run else 0


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    player1_card = [card[0]] + [card[2]]
    player2_card = [card[1]] + [card[3]]
    card = card[4::]

    for j in range(len(card)):
        if not j & 1:
            player1_card += [card[j]]
            player1 = check_babygin(player1_card)
            if player1 and not player2:
                print('#{} 1'.format(tc))
                break
        else:
            player2_card += [card[j]]
            player2 = check_babygin(player2_card)
            if player2 and not player1:
                print('#{} 2'.format(tc))
                break
    if player1 == player2:
        print('#{} 0'.format(tc))




