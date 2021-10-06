import sys
sys.stdin = open('sample_input.txt')

def game(li):
    card = [0]*10
    for i in range(len(li)):
        card[li[i]] += 1
        if card[li[i]]==3:      # Triplet
            return True

    for j in range(8):
        if card[j]>=1 and card[j+1]>=1 and card[j+2]>=1:    # Run
            return True


T = int(input())

for tc in range(1, T+1):
    card = list(map(int,input().split()))

    p1 = []
    p2 = []
    for i in range(0,12,2):
        p1.append(card[i])
        p2.append(card[i+1])

        if i >=4:
            play1 = game(p1)
            play2 = game(p2)
            if play1:
                winner = 1
                break
            if play2:
                winner =2
                break
    else:
        winner = 0
    print('#{} {}'.format(tc, winner))