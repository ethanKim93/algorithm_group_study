# 풀어야함

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    T = int(input())
    N, B = map(int, input().split())  # N: 점원수 / B: 선반높이
    height = list(map(int, input().split()))

    for i in range(1 << N -1):
        for j in range(N):
            if i & (1 << j):

