import  sys
sys.stdin=open('input.txt')
T=int(input())

for tc in range(1,T+1):
    M=int(input())

    arr=[list(map(int,input().split())) for _ in range(M)]
        #상하우좌
    xd=[0,0,1,-1]
    yd=[-1,1,0,0]
    result=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(xd)):
                now=arr[i][j]
                X=xd[k]+i
                Y=yd[k]+j
                if 0<=X<len(arr) and 0<=Y<len(arr):
                    result+=abs(arr[X][Y]-now)

    print(result)