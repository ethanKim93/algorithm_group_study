import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input()) #길이
    buildings = list(map(int, input().split()))
    
