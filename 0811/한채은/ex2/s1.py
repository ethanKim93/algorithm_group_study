import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)

    for i in range(1, 1<<n):        # 공집합을 고려하지 않을 거라 1부터 시작
        part = 0
        for j in range(n):
            if i & (1<<j):          # value 값을 꺼내서 넘겨주기
                part += arr[j]

        if not part:
            print(1)
            break

    else:
        print(0)
