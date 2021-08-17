import sys

sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())

for i in range(0, T):
    N, M = input().split()
    cnt = 0  # M 문자열이 N에 몇번 들어가있는지 체크
    search = 0  # while문을 돌리기 위한 값
    while search + len(M) <= len(N):    # word에 넣는 문자열이 N을 넘어가지 않도록 제한
        word = ''  # N의 특정 문자열을 확인하기 위한 변수
        for k in range(0, len(M)):
            word += N[search + k]       # word에 M의 길이만큼 문자를 더해서 비교할 문자열 만들기
        if word == M:       # 비교할 문자열과 동일할경우
            cnt += 1
            search += len(word)     # 문자열 비교 후 중복을 피하기 위해 다음 문자부터 검색한다.
        else:           # 동일하지 않은경우
            search += 1
    print('#{} {}'.format(i + 1, (len(N) - len(M) * cnt) + cnt))
    # 입력할 타자 횟수는 전체 문자열 길이 - (비교 문자형 길이 * 중복횟수 + 중복횟수)
    # (비교 문자형 길이 * 중복횟수 + 중복횟수) : M 문자열을 1번의 타자로 입력 가능하게 하므로 해당 문자열의 타자 횟수를 1로 만든다.
