import sys
sys.stdin = open('sample_input.txt')


def grouping(group):
    if len(group) == 1:
        return group[0]
    elif len(group) == 2:
        return tournament(group[0], group[1])
    else:
        mid = (len(group)+1)//2
        group1 = group[:mid]
        group2 = group[mid:]
        return tournament(grouping(group1), grouping(group2))


def tournament(c1, c2):
    if c1[1] == c2[1] or (c1[1] == 2 and c2[1] == 1) or (c1[1] == 3 and c2[1] == 2) or (c1[1] == 1 and c2[1] == 3):
        return c1
    else:
        return c2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    players = []
    for player, card in enumerate(cards):
        players.append([player + 1, card])

    print('#{} {}'.format(tc, grouping(players)[0]))


