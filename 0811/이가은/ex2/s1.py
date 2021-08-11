import sys
sys.stdin = open('input.txt')

test_cases = int(input())
for test in range(test_cases):
    arr = list(map(int,input().split()))
    n = len(arr)

    for i in range(1, 1<<n):    # 1<<n : 부분집합의 개수 == 2**n # 1부터 시작하면 '0일 때:공집합'은 안보게됨
        part = 0
        for j in range(n):     # 원소의 수만큼 비트를 비교함
            if i & (1<<j):      # i=0 일 때 0&x라서 아무것도 안함
                part += arr[j]
        if not part:
            print(1)
            break
    else:
        print(0)