import sys
sys.stdin = open('sample_input.txt')

Test_case = int(input())
for test in range(Test_case):
    num_cnt = int(input())
    num_arr = map(int, input().split())

    special_arr