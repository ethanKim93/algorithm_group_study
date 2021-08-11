import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(T):
    nums = list(map(int, input().split()))

    for i in range(1, 1<<10):
        total = 0
        for j in range(11):
            if i & (1<<j):
                total += nums[j]
        if not total:
            print('#{} 1'.format(tc))
            break
    else:
        print('#{} 0'.format(tc))