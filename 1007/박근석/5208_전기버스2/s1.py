import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def back_tracking(N, M, load):
    global cnt
    min1 = 0
    visited = [0]*(len(M)-1)
    if load == len(M):
        if min1 < cnt:
            cnt = min1
            return

    else:

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    M = arr[1:] + [0]
    cnt = len(M)-1
    back_tracking(1)