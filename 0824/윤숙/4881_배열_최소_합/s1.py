#틀은 잡았는 데 구현 고민중입니다..
def sumNumber(k,visited):
    if k>N:
        return
    if k==N:
        pass
    for i in range(N):
        if vistied[i]==0: #방문하지 않아서 방문할때
            #....
            sum+=numbers[k][i]
            vistied[i]=1
            # sumNumber(k+1,vistied)
        else : #방문한 상태일때..
            pass
            #....

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):

    N=int(input())
    numbers=[list(map(int,input().split())) for _ in range(N)]
    vistied=[[0]*N for _ in range(N)]
    k = 0
    print(sumNumber(k,vistied))