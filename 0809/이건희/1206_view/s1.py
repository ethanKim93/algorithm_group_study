import sys
sys.stdin = open('input.txt')

for tc in range(10):
    nums = int(input())
    buildings = list(map(int,input().split()))
    print(nums)
    print(buildings)