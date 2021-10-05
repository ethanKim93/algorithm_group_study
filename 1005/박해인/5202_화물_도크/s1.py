import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    data.sort(key=lambda x: x[1])
