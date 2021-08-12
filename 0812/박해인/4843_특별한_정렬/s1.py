import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 정수의 개수 N 10<=N<=100
    ai = list(map(int, input().split())) # N개의 정수를 담은 리스트ai 1<=ai<=100
