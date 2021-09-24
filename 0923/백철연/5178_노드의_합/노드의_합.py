import sys
sys.stdin = open('sample_input.txt')



T = int(input())
for _ in range(T):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)

    for tc in range(1, M+1):
        node, value = map(int, input().split())
        arr[node] = value

    print(arr)
    while i < 0 :
