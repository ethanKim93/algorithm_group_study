import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    # Brute Force
    len_a = len(a)     # 전체 패턴으ㅣ길이
    len_b = len(b)     # 찾을 패턴의 길이
    cnt = 0
    i = 0    # b의 인덱스
    j = 0    # a의 인덱스
    while i < len_a and j < len_b:
        if a[i] != b[j]:    # 패턴 매칭 실패시
            i -= j         # i인덱스는 시작점으로
            j = -1         # j인덱스는 원점으로
        i += 1
        j += 1
        if j == len(b):
            cnt += 1
            j = 0
    result = (len(a)+cnt) - len(b)*cnt   # 패턴이 매칭된 수만큼 전체의 길이에서 빼줌
    print(result)

















