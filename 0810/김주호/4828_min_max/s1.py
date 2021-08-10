import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for case in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    min_num = nums[0]
    max_num = nums[0]

    for i in range(1, N):
        if min_num > nums[i]:
            min_num = nums[i]
        elif max_num < nums[i]:
            max_num = nums[i]

    print("#{} {}".format(case + 1, max_num - min_num))