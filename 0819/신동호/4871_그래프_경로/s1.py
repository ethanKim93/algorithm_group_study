import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    matrix = [[0] * (V+1)] * (V+1)
    [list(map(int, input().split())) for _ in range(E)]
    print(matrix)