import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mid = N//2
    arr = [list(map(int, input().rstrip())) for _ in range(N)]
    ans = []

    for i in range(mid):
        ans += arr[i][mid-i:N-(mid-i)]
        ans += arr[N-1-i][mid-i:N-(mid-i)]
    ans += arr[mid]

    print('#{}'.format(tc), end=' ')
    total = 0
    for num in ans:
        total += num
    print(total)
