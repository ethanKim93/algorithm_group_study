import sys
sys.stdin = open('input.txt')

T=int(input())

for tc in range(1,T+1):
    width = int(input())
    heights = list(map(int,input().split()))
    for i in range(width):
        fall = width-1-i
        stack = 0
        for j in range(i+1,heights):
            if heights[i] <= heights[j]:
                stack += 1


