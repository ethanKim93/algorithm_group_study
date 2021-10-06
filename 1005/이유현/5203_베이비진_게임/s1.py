import sys
sys.stdin = open('sample_input.txt')


def isBabyGin(cnt_list):
    global ans
    if 3 in cnt_list:
        return True
    else:
        for i in range(0, 8, 1):
            if cnt_list[i] >= 1 and cnt_list[i+1] >= 1 and cnt_list[i+2] >= 1:
                return True


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    ans = 0
    while cards:
        player1[cards.pop(0)] += 1
        player2[cards.pop(0)] += 1

        if sum(player1) > 2:
            if isBabyGin(player1):
                ans = 1
                break

        if sum(player2) > 2:
            if isBabyGin(player2):
                ans = 2
                break

    print('#{} {}'.format(tc, ans))