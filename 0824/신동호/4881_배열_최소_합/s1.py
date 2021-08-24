import sys
sys.stdin = open('sample_input.txt')

def check(mat, N):
    pass

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    stack = [for i in range(0, N)]
    print(stack)