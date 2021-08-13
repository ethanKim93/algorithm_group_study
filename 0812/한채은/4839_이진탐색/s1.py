import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    start = 1   # 처음 책 페이지
    end = P     # 끝나는 페이지
    cnt_A = 0   # A가 지정된 페이지를 찾는 횟수
    cnt_B = 0   # B가 지정된 페이지를 찾는 횟수

    while True:
        mid = (start + end) // 2    # 중간값
        cnt_A += 1      # cnt_A에 1 더해주기
        if mid == Pa:   # 만약에 중간 페이지가 내가 찾는 페이지랑 같으면
            break       # 멈추기
        elif mid <= Pa:     # 중간 값 보다 찾는 페이지가 더 크면
            start = mid     # 처음 페이지를 중간으로 놓고 다시 구하기
        else:
            end = mid       # 아니면 끝나는 페이지를 중간으로 놓고 다시 구하기

    start = 1
    end = P

    while True:
        mid = (start + end) // 2
        cnt_B += 1
        if mid == Pb:
            break
        elif mid <= Pb:
            start = mid
        else:
            end = mid

    if cnt_A > cnt_B:   # 만약 A가 B보다 횟수가 더 많으면 A가 진거
        print('{} {}'.format(tc, 'B'))  # 이긴 사람 출력하는 거니까 B 출력
    elif cnt_A < cnt_B:
        print('{} {}'.format(tc, 'A'))
    else:
        print('{} {}'.format(tc, 0))    # 두 경우가 아니라면 비긴거니까 0 출력