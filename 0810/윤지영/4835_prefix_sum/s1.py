import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    num = list(map(int, input().split()))
    N, M = num[0], num[1]
    ai = list(map(int, input().split()))
    for i in range(N-M+1):   # 마지막 범위를 인덱스에러 없이 돌기 위한 범위
        s = 0
        for j in range(i, i+M):
            s += ai[j]
            if not i:
                section_max = s
                section_min = s
        if section_min > s:
            section_min = s
        elif section_max < s:
            section_max = s
    print('#{0} {1}'.format(tc, section_max-section_min))