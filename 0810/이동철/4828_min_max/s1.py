import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    num = int(input())
    case_num = list(map(int, input().split()))
    max_case = case_num[0]
    min_case = case_num[0]
    result = 0
    for n in range(1, len(case_num)):
        if max_case < case_num[n]:
            max_case = case_num[n]
        if min_case > case_num[n]:
            min_case = case_num[n]
    result = max_case - min_case
    print('#{} {}'.format(tc, result))
