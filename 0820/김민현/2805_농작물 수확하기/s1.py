import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    ground = [list(input()) for _ in range(N)]

    #print(ground)
    ans = 0
    for i in range(N):
        if i <= N//2:
            for j in range(N//2-i,N//2+i+1):
                    ans += int(ground[i][j])
        else:
            for j in range(i-N//2,N-i+N//2):
                    ans += int(ground[i][j])
        a = 1
    print('#{} {}'.format(tc,ans))

