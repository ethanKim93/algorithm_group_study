import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    result = 0                      # 타이핑 횟수
    i = j = 0                       # A의 인덱스 i, B의 인덱스 j
    N, M = len(A), len(B)
    while i < N:
        if A[i] != B[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == M:                  # 패턴이 일치하면
            A = A[:i-M] + A[i:]     # 문자열에서 패턴 제거
            result += 1             # 타이핑 횟수 추가
            i = j = 0               # 인덱스 초기화
            N = len(A)              # N 길이 초기화
    result += N                     # 더이상 패턴과 일치하지 않으면 나머지 글자수 만큼 타이핑 횟수 추가

    print('#{} {}'.format(tc, result))
