import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N = int(input())
    result = [[0] * N for i in range(N)]
    i, j, index = 0, -1, 0
    dir = ['r', 'l', 'u', 'd']


