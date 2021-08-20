import sys

sys.stdin = open('input.txt','r',encoding='cp949')
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total=0
    for i in range(N):
        cnt=0
        for j in range(N):
            if i<N and j<N and arr[i][j]==1:
                cnt+=1
            else:
                if cnt==K:
                    total+=1
                cnt=0

        if cnt==K:
            total+=1
            cnt=0

    for i in range(N):
        cnt=0
        for j in range(N):
            if i<N and j<N and arr[j][i]==1:
                cnt+=1
            else:
                if cnt==K:
                    total+=1
                cnt=0

        if cnt==K:
            total+=1
            cnt=0














    print(total)
