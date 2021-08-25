import sys
sys.stdin = open('sample_input.txt')


def rsp(p1, p2):
    if p1[1] == p2[1]:
        return p1
    elif p1[1] == 1 and p2[1] == 2:
        return p2
    elif p1[1] == 1 and p2[1] == 3:
        return p1
    elif p1[1] == 2 and p2[1] == 1:
        return p1
    elif p1[1] == 2 and p2[1] == 3:
        return p2
    elif p1[1] == 3 and p2[1] == 1:
        return p2
    elif p1[1] == 3 and p2[1] == 2:
        return p1


def tournament(players):
    n = len(players)
    if n == 1:
        return players[0]
    elif n == 2:
        return rsp(players[0], players[1])
    else:
        if n % 2:
            return rsp(tournament(players[:n//2+1]), tournament(players[n//2+1:]))
        else:
            return rsp(tournament(players[:n//2]), tournament(players[n//2:]))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    players = []
    for player, card in enumerate(cards):
        players.append((player+1, card))
    print('#{} {}'.format(tc, tournament(players)[0]))
