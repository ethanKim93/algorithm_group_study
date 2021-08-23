import sys
sys.stdin = open('input.txt')

test_cases = int(input())

for test in range(test_cases):
    n = int(input())

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    snail = [[0]*5]*5
    nums = n * n

    for num in range(1, nums+1):
