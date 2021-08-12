import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(0, T):
    N = int(input())  # = len(A)
    A = list(map(int, input().split()))
    New = []        # 리스트 결과값
    result = ""     # 출력할 결과값
    for j in range(1, N):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:    # 버블정렬로 리스트 선 정렬
            A[i + 1] = A[i]
            i -= 1
            A[i + 1] = key

    for i in range(0, 5):   # 정렬 결과를 10개까지 출력 / 한번 for문이 돌 때마다 가장 작은값과 큰 값을 리스트에 추가
            New.append(A[N - i - 1])   # N이 20이고 i가 5일경우 A[20-5-1] 이므로 A[14]
            New.append(A[i])    # A[5]

    for k in range(len(New)):
        result += (str(New[k]) + " ")

    print("#{} {}".format(tc+1, result))
