import sys
sys.stdin=open('GNS_test_input.txt')


def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    nums = input().split()

    decode = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    for i in range(N):
        nums[i] = decode[nums[i]]

    result = selection_sort(nums)

    incode = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
    for i in range(N):
        result[i] = incode[result[i]]

    print(tc)
    print(*result, sep=' ')