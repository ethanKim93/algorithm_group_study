import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    answer = [0] * 5
    primes = [2, 3, 5, 7, 11]
    for idx, prime in enumerate(primes):
        while True:
            if not N % prime:
                N //= prime
                answer[idx] += 1
            else :
                break

    print('#{}'.format(test_case), end=' ')
    print(*answer)