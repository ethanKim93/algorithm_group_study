# 푸는중

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    corr = []
    for _ in range(N):
        student = []
        start, end = map(int, input().split())
        corr.append([start // 2, end // 2 + 1])
    print(corr)