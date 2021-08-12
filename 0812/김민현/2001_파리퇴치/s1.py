import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = list(map(int,input().split()))   
    ai = list(map(int,input().split()))