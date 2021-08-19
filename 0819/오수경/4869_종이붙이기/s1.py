import sys
sys.stdin = open('sample_input.txt')


def my_factorial(n):    # 팩토리얼 함수 정의
    if n > 1:
        return n * my_factorial(n - 1)
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = int(N / 10)


    two_num = n//2  # 20*20 짜리 종이가 사용될 수 있는 최대 갯수

    cnt = 0

    for two in range(two_num+1):    # 20*20 종이가 쓰인 갯수 (0개, 1개 ...)
        if two == 0:                # 20*20 종이가 0개 = 모두 10*20으로만 구성된 경우
            cnt += 1
        else:
            one_num = n - 2*two     # 10*20가 사용된 갯수
            sort_num = my_factorial(one_num+two)/(my_factorial(one_num)*my_factorial(two))  # 전체 사용된 종이 배열 경우의 수
            two_one = 2**two        # 20*20종이 -> 10*20종이 변환 가능 고려 경우의 수
            cnt += sort_num*two_one # 전체 경우의 수 = (배열 경우의 수) * (20*20 -> 10*20 변환 경우의 수)

    print('#{} {}'.format(tc, int(cnt)))