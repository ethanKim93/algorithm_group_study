
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lis = list(map(int, input().split()))

    for i in range(0, len(lis)-1):
        minindex = i
        for j in range(i+1, len(len(lis)):




