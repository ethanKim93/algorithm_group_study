import sys
sys.stdin = open("sample_input.txt")

def rcp(i,j): #p1이 더 빠른 번호
    p1 = card[i]
    p2 = card[j]
    if p1 == 1:
        if p2 == 2:
            return j
        else:
            return i
    elif p1 == 2:
        if p2 == 3:
            return j
        else:
            return i
    elif p1 == 3:
        if p2 == 1:
            return j
        else:
            return i

def div(start,end):
    if start + end == 1:
        return rcp(start,end)
    return rcp(div(start,(start+end)//2),
    div(((start+end)//2)+1,end))




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = list(map(int,input().split()))

    print('#{} {}'.format(tc,div(0,len(card))))

