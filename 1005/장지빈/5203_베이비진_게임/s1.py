import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    deck = list(map(int, input().split()))
    ans = 0
    Acnt = [0]*12
    Bcnt = [0]*12

    for i in range(len(deck)):
        if not(i % 2):
            Acnt[deck[i]] += 1
            if Acnt[deck[i]] ==3:
                ans = 1
                break
            elif i>2 and (Acnt[deck[i]] and Acnt[deck[i]+1] and Acnt[deck[i]+2]) or (Acnt[deck[i]-1] and Acnt[deck[i]] and Acnt[deck[i]+1]) or (Acnt[deck[i]-2] and Acnt[deck[i]-1] and Acnt[deck[i]]):
                ans = 1
                break
        else:
            Bcnt[deck[i]] += 1
            if Bcnt[deck[i]] ==3:
                ans = 2
                break
            elif i>2 and (Bcnt[deck[i]] and Bcnt[deck[i]+1] and Bcnt[deck[i]+2]) or (Bcnt[deck[i]-1] and Bcnt[deck[i]] and Bcnt[deck[i]+1]) or (Bcnt[deck[i]-2] and Bcnt[deck[i]-1] and Bcnt[deck[i]]):
                ans = 2
                break

    print('#{} {}'.format(tc, ans))