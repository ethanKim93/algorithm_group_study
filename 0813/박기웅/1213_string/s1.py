def BruteForce(P, strs):
    i = j = cnt = 0 # i 는 strs의 인덱스, j 는 P의 인덱스, cnt 는 패턴 일치 개수
    M = len(P)
    N = len(strs)
    while j < M and i < N:
        if strs[i] != P[j]:
            i = i - j #비교를 시작한 위치
            j = -1    # 초기화
        i += 1 # 그 다음칸으로 이동
        j += 1 # 초기화

        if j == M:
            cnt += 1
            j = 0 # 맞은 경우 초기화
    return cnt

import sys
sys.stdin = open("test_input.txt", encoding='UTF8')

for _ in range(10):
    tc = int(input())
    P = input()
    strs = input()
    print('#{} {}'.format(tc, BruteForce(P, strs)))
