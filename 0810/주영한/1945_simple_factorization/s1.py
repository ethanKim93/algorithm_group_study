import sys
sys.stdin = open('input.txt')

T = int(input())
factors = [2, 3, 5, 7, 11]
for tc in range(1, T + 1):
    # 결과를 저장할 리스트를 생성한다.
    times = [0] * 5
    number = int(input())

    # 각 인자에 대해 나누어 떨어지지 않을 때 까지 나누어 주고, 이를 times에 최신화 한다.
    for idx, factor in enumerate(factors):
        while not (number % factor):
            number = number // factor
            times[idx] += 1

    times = " ".join(map(str,times))
    print("#{} {}".format(tc, times))

