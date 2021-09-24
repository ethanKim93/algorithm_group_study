import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = [0] + list(map(int, input().split()))
    for i in range(2,N+1):
        while num[i] < num[i//2]:
            num[i], num[i//2] = num[i//2], num[i]
            i //= 2
    answer = 0
    while N > 0:
        N //= 2
        answer += num[N]
    print('#{} {}'.format(tc,answer))
