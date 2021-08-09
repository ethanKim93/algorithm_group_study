import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    width = int(input())
    height = list(map(int, input().split()))
    print(height)