import sys
sys.stdin = open('input.txt')

T = int(input())

def shift(n):
    for i in range(n):
        if not M & (1 << i):
            return 'OFF'
    return 'ON'


for tc in range(1, T+1):
    N, M = map(int, input().split())
    print("#{} {}".format(tc, shift(N)))