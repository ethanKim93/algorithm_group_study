# 부분집합의 합을 만드는 문제
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = 10
# sel = [0] * n


k=0
def sumNumber(k,visited):
    if k>=N:
        return
    for i in range(N):
        if vistied[i]==0:
            sum+=numbers[k][i]
            vistied[i]=1

            sumNumber(k+1,vistied)

    k+=1
import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):

    N=int(input())
    numbers=[list(map(int,input().split())) for _ in range(N)]
    vistied=[[0]*N for _ in range(N)]

    sumNumber(k,vistied)