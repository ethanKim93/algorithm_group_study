import sys
sys.stdin = open("s_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))




    ans = nums
    print('#{} {}'.format(tc,ans))