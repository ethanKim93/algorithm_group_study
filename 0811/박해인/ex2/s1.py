import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))


    # n = len(arr)
    #
    # for i in range(1 << n): # 2^2
    #     for j in range(n+1):
    #         if i & (i << j): # i의 j번째 비트가 1인지 아닌지 리턴
    #             print(i, end=", ")

