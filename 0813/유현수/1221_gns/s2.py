# 반장님 코드 따라해봤습니다.
import sys
sys.stdin=open('GNS_test_input.txt')

T = int(input())
for _ in range(T):
    tc, n = input().split()
    n = int(n)
    nums = input().split()

    decode = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = []

    for i in range(len(decode)):
        for j in range(n):
            if decode[i] == nums[j]:
                result.append(nums[j])

    print(tc)
    print(*result, sep=' ')