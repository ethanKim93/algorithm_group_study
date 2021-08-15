import sys
sys.stdin=open('sample_input.txt')
T= int(input())

for tc in range(1,T+1):
    N=int(input())
    color_sum=0
    arr = [[0] * 10 for _ in range(10)]
    for i in range(N):

        sx,sy,ex,ey,color = map(int,input().split())
        for j in range((ex-sx)+1):
            for k in range((ey-sy)+1):
                arr[sx+j][sy+k]+=color

    C=0
    #보라색일때가 아닌 111도 가능하게 만들어보기
    for l in range(10):
        for m in range(10):
            if arr[l][m]==3:
                C+=1
    print('#{} {}'.format(tc,C))