import sys
sys. stdin = open('input.txt')

T= int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)

    for i in range(1, 1<<n):
        part = 0
        for j in range(n):
            if i & (1<<j):
                part += arr[j]
        if not part:
            print(1)
            break
    else:
        print(0)

