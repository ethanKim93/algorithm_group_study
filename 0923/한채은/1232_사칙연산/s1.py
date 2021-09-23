import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))