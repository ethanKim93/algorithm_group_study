import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    i = 0
    a = [1]
    print(f'#{tc}')
    while(i<N):
        print(*a)
        a = [l+r for (l,r) in zip([0]+a,a+[0])]
        i+=1