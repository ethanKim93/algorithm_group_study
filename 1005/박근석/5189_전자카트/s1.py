import sys
sys.stdin = open('input.txt')

T = int(input())

def sum1(n):





for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(N)]
    ans = N*100
    min = 0
    used = (N-1)*[0]
    sum1(N)