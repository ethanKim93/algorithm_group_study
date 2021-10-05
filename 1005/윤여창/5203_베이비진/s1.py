import sys
sys.studin = open('input.txt')

T = int(input())

def check(player):
    for j in range(10):
        if player[j] == 3:
            return True
    for k in range(8):
        if player[k] and player[k + 1] and player[k + 2]:
            return True
    return False


for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0
    for i in range(len(card)):
        if not i % 2:
            p1[card[i]] += 1
            if check(p1):
                winner = 1
                break
        else:
            p2[card[i]] += 1
            if check(p2):
                winner = 2
                break

    print("#{} {}".format(tc, winner))