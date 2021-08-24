import sys
sys.stdin = open('sample_input.txt')

def tourn(pep):
    n = len(pep)
    g1 = pep[:(1 + n) // 2]
    g2 = pep[(1 + n) // 2:]
    if len(g1) == 1 and len(g2) == 1:
        if card_dict[g1[0]] == 1 and card_dict[g2[0]] == 2:
            return g2[0]
        if card_dict[g1[0]] == 2 and card_dict[g2[0]] == 3:
            return g2[0]
        if card_dict[g1[0]] == 3 and card_dict[g2[0]] == 1:
            return g2[0]
        else:
            return g1[0]
    elif len(g2) == 0:
        return g1[0]
    return tourn([tourn(g1), tourn(g2)])




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    card_dict = {}
    people = []
    for i in range(1, N+1):
        card_dict[i] = cards[i-1]
        people += [i]
    print('#{} {}'.format(tc, tourn(people)))
