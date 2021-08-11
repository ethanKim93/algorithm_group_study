import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)

    for i in range(1, 1 << n):  # == 2^n (1<<n) 말고 (1, 1 << n)으로 하면 공집합 제외하고 확인함.
        part = 0
        for j in range(n):  # j는 0부터 9까지 1씩 증가한다.
            if i & (1 << j):  # i의 j번째 비트가 1인지 아닌지 리턴
                part += arr[j]
        if part == 0:
            print(1)
            break
    else:
        print(0)

