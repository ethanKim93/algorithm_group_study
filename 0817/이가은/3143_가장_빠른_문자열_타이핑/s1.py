import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test in range(T):
    A, B = input().split()
    N = len(A)
    M = len(B)
    i = 0 # 시작 index
    cnt = N # 타이핑 횟수

    while i < N-M+1 : # 글자의 끝까지 확인할 범위
        if A[i:i+M] == B:
            i += M # B 만큼의 글자가 있다면 확인 시작할 i를 B의 글자수 M만큼 증가
            cnt -= M-1 # cnt에서 M번을 1번만 타이핑 하면 됩니다.
        else:
            i += 1 # A와 B가 일치하지 않으면 확인할 index i를 1씩 증가시킵니다.

    print('#{} {}'.format(test+1, cnt))