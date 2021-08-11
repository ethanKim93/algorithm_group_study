import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    ls1 = list(map(int, input().split()))
    print(ls1)

    n = len(ls1)
    sums1 = 0
    sums2 = 0

    for i in range(1, 1<<n):   #2**n 해도 상관없음 # 0~1023
        part = 0
        for j in range(n):
            if i & (1<<j):
                part += ls1[j]
        if not part:
            print(1)
            break
    else:
        print(0)



