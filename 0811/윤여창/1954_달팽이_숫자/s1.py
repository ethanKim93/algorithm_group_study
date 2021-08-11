import sys
sys.stdin = open('input.txt')


di = [0,1,0,-1]
dj = [1,0,-1,0]
                                     # 라이브 강의 때 알려주신대로 했습니다.
T = int(input())

for tc in range(1,T+1):
    N = int(input())

    arr = [[0]*N for i in range(N)]
    cunt = 1
    dire = 0
    i, j = 0,-1

    while cunt <= N*N:
        newi, newj = i + di[dire], j+dj[dire]
        if 0<=newi<N and 0<=newj<N and arr[newi][newj] ==0:
            arr[newi][newj] = cunt
            cunt += 1
            i,j =newi,newj
        else:
            dire = (dire + 1) % 4
    print('#{} {}'.format(tc, arr))
