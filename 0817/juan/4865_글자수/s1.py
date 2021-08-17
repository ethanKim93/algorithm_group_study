T = int(input())

for tc in range(1, T+1):
    N = set(list(input()))              # set 로 중복 제거
    M = input()
    str_cnt = {}                        # 글자 당 글자수 저장할 딕셔너리
    max_val = 0                         # 최대값 초기화

    for n in N:
        for m in M:
            if n == m:                  # N과 M에서 같은 글자가 나오면 딕셔너리에 추가
                if n in str_cnt:
                    str_cnt[n] += 1
                else:
                    str_cnt[n] = 1

    for value in str_cnt.values():      # str_cnt 딕셔너리 value 중 가장 큰 값을 출력
        if value > max_val:
            max_val = value
    print('#{} {}'.format(tc, max_val))