import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxK = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            FK = 0
            for x in range(M):
                for y in range(M):
                    FK += arr[i+x][j+y]
                    if FK > maxK:
                        maxK = FK

    print('#{} {}'.format(tc, maxK))