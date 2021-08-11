import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    result = 0
    subset = []
    for i in range(1, 1 << len(arr)):
        sub_sum = 0
        for j in range(len(arr)):
            if i & (1 << j):
                sub_sum += arr[j]
        subset.append(sub_sum)
        for k in subset:
            if k == 0:
                result = 1
    print('#{} {}'.format(tc, result))
