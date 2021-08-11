import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    total = []

    for i in range(1, 1 << n):  # 공집합인 경우를 제외하기 위해 i를 1부터 시작하게 한다
        part = 0
        for j in range(n):
            if i & (1<<j):
                part += arr[j]
        if not part:
            result = 1
            break   # 부분집합을 구할 때마다 부분집합의 합을 구하고 그 값이 0이 되면 break
    else:
        result = 0  #반복문을 모두 돌아도 부분집합의 합이 0이 안나온다면 0을 return
    print('#{} {}'.format(tc, result))
