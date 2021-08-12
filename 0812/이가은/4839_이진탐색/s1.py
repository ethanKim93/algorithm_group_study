import sys
sys.stdin = open('sample_input.txt')

test_cases = int(input())
for test in range(test_cases):
    P, Pa, Pb = map(int,input().split())

    start_a = start_b = 1
    end_a = end_b = P
    cnt_A = cnt_B = 0

    # Pa 값 찾는 연산
    while True:
        if Pa == P or Pa == 1: # 만약 Pa가 시작/끝 값이면 바로 break
            break
        else:
            page = start_a + (end_a-start_a)//2
            if Pa > page:
                start_a = page
                cnt_A +=1
            else:
                end_a = page
                cnt_A +=1
            if page == Pa:
                break

    # Pb 값 찾는 연산
    while True:
        if Pb == P or Pb ==1:
            break
        else:
            page = start_b + (end_b - start_b)//2
            if Pb > page:
                start_b = page
                cnt_B +=1
            else:
                end_b = page
                cnt_B +=1
            if page == Pb:
                break

    # 승자 정하는 코드
    if cnt_A > cnt_B:
        winner = 'B'
    elif cnt_A == cnt_B:
        winner = 0
    else:
        winner = 'A'

    print('#{} {}'.format(test+1, winner))