#시간이 너무 오래 걸림 런타임 오류
import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    nums = list(map(int,input().split()))
    i = 0
    total = 0

    while i < N:
        sub = 0
        for j in range(i+1,N):
            if sub < nums[j]-nums[i]:
                sub = nums[j] - nums[i]
        total += sub
        i += 1
    print('#{} {}'.format(tc,total))