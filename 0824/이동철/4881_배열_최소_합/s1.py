import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 2):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = []
    for i in range(N):
        visited[i] = 0
    