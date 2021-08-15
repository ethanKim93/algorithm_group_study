import sys
sys.stdin=open('input.txt')
T=int(input())

for tc in range(1,T+1):
    #N은 배열
    #M은 파리채
    N,M=map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    maxV = 0
    for i in range((N-M)+1):
        for j in range((N-M)+1):
            cac=0
            for  k in range(M):
                for l in range(M):
                    cac+=arr[i+k][j+l]

            if cac>maxV:
                maxV=cac

    print('#{} {}'.format(tc,maxV))














