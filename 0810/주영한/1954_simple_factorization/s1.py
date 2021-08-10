import sys
sys.stdin = open('input.txt')

T = int(input())
factors = [11, 7, 5, 3, 2]

for tc in range(1, T + 1):
    times = [0] * 5
    number = int(input())
    for idx, factor in enumerate(factors):
        while not (number % factor):
            number = number // factor
            times[5 - idx - 1] += 1
    times = " ".join(map(str,times))
    print("#{} {}".format(tc, times))

