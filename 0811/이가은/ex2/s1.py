import sys
sys.stdin = open('input.txt')

test_cases = int(input())
for test in range(test_cases):
    test_nums = list(map(int,input().split()))
    num_cnt = len(test_nums)


    for i in range(1<<num_cnt):    # 1<<n : 부분집합의 개수
        for j in range(num_cnt+1):     # 원소의 수만큼 비트를 비교함
            print(i &(1<<j))
            if i & (1<<j):
                part_sum += test_nums[j]

