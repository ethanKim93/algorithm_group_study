import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    result = len(A) # 최악의 경우 A 전체 타이핑
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] != B[j]: # 불일치시
            i -= j # i 돌아가고
            j = -1 # j도 처음부터
        i += 1
        j += 1
        if j == len(B): # j 전부 일치
            j = 0 # j 초기화
            result -= len(B) - 1 # B의 길이 -1 만큼 횟수 감소
    print('#{} {}'.format(tc, result))
    # print(A, B)
    # A = A.replace(B, ' ')
    # print(A)