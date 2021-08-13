sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [number for number in range(1, 13)] # 1~12까지 숫자로 구성된 배열 생성
    total = 0
    for i in range(1 << len(arr)):
        numsum = 0 # 부분집합 원소의 합
        cnt = 0 # 부분집합 원소개수
        for j in range(len(arr)):
            if i & (1 << j):
                numsum += arr[j]
                cnt += 1
        if numsum == K and N == cnt: # 부분집합 원소의 합이 K 원소의 개수가 cnt이면 total 1 증가
            total += 1
    print('#{} {}'.format(tc, total))