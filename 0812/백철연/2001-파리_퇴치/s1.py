import sys
sys.stdin = open('input.txt')

di = [0, 1, 0, -1] #오른쪽부터 시계방향 순
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    square = [list(map(int, input().split())) for _ in range(N)]
    print(square)