import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    width = int(input())
    heights = list(map(int, input().split()))
    print(heights)