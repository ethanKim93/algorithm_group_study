import sys
sys.stdin = open('input.txt')

T = int(input())

def vs(start, end):
    if start == end:
        return end
    left = vs(start, (start+end)//2)
    right = vs((start+end)//2+1, end)
    return winner(left, right)
def winner(l,r):
    if (tournament[l] - tournament[r])%3 <2 :
        return l
    return r

for tc in range(1,T+1):
    N = int(input())
    tournament = [0]+list(map(int,input().split()))

    print('#{} {}'.format(tc,vs(1,N)))