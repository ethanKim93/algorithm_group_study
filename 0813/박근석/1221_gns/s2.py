import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
numsys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(1, T+1):
    tc, nums = input().split()
    text = input().split()
    GNS = {}

    for num in text:
        if num in GNS:
            GNS[num] += 1
        else:
            GNS[num] = 1

    print('{}')