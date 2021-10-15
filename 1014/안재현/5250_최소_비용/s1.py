import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for test_case in range(T):
    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]