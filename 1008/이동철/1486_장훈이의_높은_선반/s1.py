import sys
sys.stdin = open('input.txt', 'r')


# 부분집합을 만들어서 조건에 맞는 탑 높이를 찾는 함수
def powerset(k, N):             # k는 시작 인덱스, N은 집합의 크기
    global ans
    if k == N:                  # 부분집합이 완성되면
        total = 0
        for i in range(1, N+1):     # 탑 높이 구하기
            if arr[i]:
                total += S[i-1]
        if B <= total < ans:        # B보다 높은 탑 중 최솟값이라면 업데이트
            ans = total
    else:                           # 재귀를 통해 부분집합 만들기
        k += 1
        for i in range(2):
            arr[k] = i
            powerset(k, N)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    arr = [0] * (N+1)
    ans = 987654321
    powerset(0, N)
    print('#{} {}'.format(tc, ans-B))


# 정명수
# import sys
# sys.stdin = open('input.txt')
#
#
# def looking(n,height):
#     global answer
#     if height >= B:
#         answer = min(answer,height-B)
#         return
#     if n >= N:
#         return
#     elif n < N:
#         looking(n+1,height+people[n])
#         looking(n+1,height)
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N, B = map(int,input().split())
#     people = list(map(int,input().split()))
#     answer = 100000
#     looking(0,0)
#     print('#{} {}'.format(tc,answer))


# 박기웅
# def backtrack(k, h):
#     global min_height
#     if h < B:
#         return    # B보다 작은 선택일 경우 중단
#
#     if k == N:
#         min_height = min(h, min_height)
#
#     else:
#         for i in range(2):
#             backtrack(k+1, h-height[k]*i)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, B = map(int, input().split())
#     height = list(map(int, input().split()))
#     min_height = 10000*N
#     backtrack(0, sum(height))
#
#     print('#{} {}'.format(tc, min_height-B))
