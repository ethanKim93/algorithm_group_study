import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    T, N = map(int,input().split())
    od = list(map(int,input().split()))

    arr = [[0]*101 for _ in range(101)]

    for pair in range(0, len(arr), 2):
        