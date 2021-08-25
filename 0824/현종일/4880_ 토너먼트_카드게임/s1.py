import sys
sys.stdin = open("sample_input.txt")

def rsp(p1, p2):
    winner = p1
    p1_card = player[p1-1]
    p2_card = player[p2-1]

    if p2_card > p1_card and p2_card - p1_card == 1:
        winner = p2
    elif p2_card < p1_card and p1_card - p2_card == 2:
        winner = p2
    return winner

def tournament(l, r):
    if l == r:
        return l
    else:
        mid = (l+r) // 2
        l = tournament(l, mid)
        r = tournament(mid+1, r)
        return rsp(l, r)

for tc in range(1, int(input())+1):
    N = int(input())
    player = list(map(int, input().split()))

    print('#{} {}'.format(tc, tournament(1, N)))



