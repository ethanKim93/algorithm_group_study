import sys
sys.stdin = open('input.txt')


# 부분집합을 만들어서 조건에 맞는 탑 높이를 찾는 함수
def powerset(k ,input):             # k는 시작 인덱스, input은 집합의 크기
    global ans
    if k == input:                  # 부분집합이 완성되면
        total = 0
        for i in range(1, N+1):     # 탑 높이 구하기
            if arr[i]:
                total += H[i-1]
        if B <= total < ans:        # B보다 높은 탑 중 최솟값이라면 업데이트
            ans = total
    else:                           # 재귀를 통해 부분집합 만들기
        k += 1
        for i in range(2):
            arr[k] = i
            powerset(k, input)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    arr = [0] * (N+1)
    ans = 987654321
    powerset(0, N)
    print('#{} {}'.format(tc, ans-B))