import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

    for i in range(1, 1<<N): # 공집합 제외
        total = 0
        for j in range(N):
            if i & (1<<j):
                total += arr[j]

        if total == 0:
            print('#{} 1'.format(tc))
            break
    else:
        print('#{} 0'.format(tc))


