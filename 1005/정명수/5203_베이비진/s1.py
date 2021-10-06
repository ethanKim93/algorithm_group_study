import sys
sys.stdin = open('input.txt')

def baby(li):
    li.sort()
    if len(li)>2:
        for j in range(len(li)-2):
            if li[j] == li[j+1] and li[j+1] == li[j+2]:
                return True
            if li[j]+1 in li and li[j]+2 in li:
                return True
        return False

T = int(input())
for tc in range(1,T+1):
    card = list(map(int,input().split()))
    one = []
    two = []
    flag = 0
    for i in range(6):
        one.append(card[2*i])
        two.append(card[2*i+1])
        if baby(one):
            flag = 1
            break
        if baby(two):
            flag = 2
            break
    print('#{} {}'.format(tc,flag))