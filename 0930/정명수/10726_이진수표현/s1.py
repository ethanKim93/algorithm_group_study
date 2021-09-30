import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    num = 2**N-1
    if num&M == num:
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))