import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
newnums = ['ZRO', "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T+1):
    N = int(input().split()[1])
    arr = list(input().split())
    cnt_arr = [0]*10
    sort_arr = []

    for num in arr:
        for idx, num2 in enumerate(newnums):
            if num == num2:
                cnt_arr[idx] += 1

    for i in range(len(cnt_arr)):
        sort_arr += [newnums[i]] * cnt_arr[i]

    print('#{}'.format(tc))
    print(*sort_arr)

