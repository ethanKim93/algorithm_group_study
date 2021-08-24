import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    num = [i for i in range(N)]
    for i in range(N):
