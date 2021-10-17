import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(matrix)