import sys
sys.stdin = open('input.txt')

def check(cnt, pos):  # cnt[]에서 run/triplet 체크
    if cnt[pos] >= 3:
        return 1
    s = max(pos - 2, 0)
    e = min(pos, 7)
    for i in range(s, e + 1):
        if i <= 7 and cnt[i] and cnt[i + 1] and cnt[i + 2]:
            return 1
    return 0

for tc in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))
    # 각 플레이어가 받은 카드들을 카운팅
    p1 = [0] * 10
    p2 = [0] * 10

    ans = 0
    # 카드들을 하나씩 분배
    for i in range(0, 12, 2):
        # p1 <- cards[i], p2 <- cards[i + 1]
        c1 = cards[i]
        c2 = cards[i + 1]
        p1[c1] += 1
        p2[c2] += 1

        # 3장 이상일때 체크하는게 의미가 있다.
        if i < 6: continue

        # p1에 대해 run/triplet 체크
        if check(p1, c1):
            ans = 1
            break
        # p2에 대해 run/triplet 체크
        if check(p2, c2):
            ans = 2
            break

    print('#{} {}'.format(tc,ans))