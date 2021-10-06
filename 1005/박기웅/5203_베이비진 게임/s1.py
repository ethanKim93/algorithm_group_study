import sys
sys.stdin = open('sample_input.txt')

def baby_gin(cnt):
    ans = 0
    i = 0
    while i < 10:
        if cnt[i] and cnt[i+1] and cnt[i+2]:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            ans += 1
        if cnt[i] > 2:
            cnt[i] -= 3
            ans += 1
        i += 1
    return ans

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    cnt1 = [0]*12
    cnt2 = [0]*12
    winner = 0
    for i in range(12):
        if i%2:
            cnt2[cards[i]] += 1
        else:
            cnt1[cards[i]] += 1
        if i >= 4:
            if baby_gin(cnt1):
                winner = 1
                break
            if baby_gin(cnt2):
                winner = 2
                break
    print('#{} {}'.format(tc, winner))
                

