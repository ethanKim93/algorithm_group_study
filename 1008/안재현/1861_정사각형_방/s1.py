import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        A = list(map(int,input().split()))
        arr.append(A)
    print(arr)

