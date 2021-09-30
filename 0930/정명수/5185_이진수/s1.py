import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N, num = input().split()
    N = int(N)*4
    num = bin(int(num,16))[2:].zfill(N)
    print('#{} {}'.format(tc,num))