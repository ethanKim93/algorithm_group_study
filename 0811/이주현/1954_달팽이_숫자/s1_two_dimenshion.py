import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    arr = [0] * N * N
    change = [1, 1, -1, -1]
    change_idx = 0
    row = 0
    col = -1

    for idx in range(N*N):
