def BruteForce(P, strs):
    i = j = cnt = 0 # i 는 strs의 인덱스, j 는 Pattern의 인덱스,
    M = len(P)
    N = len(strs)
    while j < M and i < N:
        if strs[i] != P[j]:
            i = i - j #비교를 시작한 위치
            j = -1    # 초기화
        i += 1 # 그 다음칸으로 이동
        j += 1 # 초기화

        if j == M: #한 번이라도 매칭되면 1 반환
            return 1
    return 0

import sys
sys.stdin = open("sample_input.txt")
for tc in range(1, int(input())+1):
    fst = input()
    scd = input()
    print('#{} {}'.format(tc, BruteForce(fst, scd)))