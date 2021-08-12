import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    for idx in range(1,N+1):
        arr.append(idx)

    for i in range(1, 1<<N):
        for j in range(N):
            if i & (1<<j):
                print(arr[j], end="")
        print()