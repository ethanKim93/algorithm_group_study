import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def baby(p1,p2):
    for n in range(3,len(p1)+1):
        temp1 = sorted(p1[:n])
        temp2 = sorted(p2[:n])

        for i in range(n-3):
            if (temp1[i] == temp1[i+1] == temp1[i+2]) or ((temp1[i]+1) in temp1 and (temp1[i]+2) in temp1):
                return 1
            if temp2[i] == temp2[i+1] == temp2[i+2] or ((temp2[i]+1) in temp2 and (temp2[i]+2) in temp2):
                return 2
    return 0

for tc in range(1,T+1):
    winner = 0
    p1 = []
    p2 = []
    card = list(map(int,input().split()))
    for i in range(len(card)):
        if i%2:
            p2.append(card[i])
        else:
            p1.append(card[i])

    winner = baby(p1,p2)
    print('#{} {}'.format(tc,winner))