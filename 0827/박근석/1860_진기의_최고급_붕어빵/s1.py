import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    N, M, K = map(int, input().split())
    num_list = list(map(int, list(input().split())))

