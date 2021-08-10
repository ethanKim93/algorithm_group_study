import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    Num = int(input())
    N = [2, 3, 5, 7, 11]
    result = [0] * 5
    for number in range(5):
        while Num % N[number] == 0:
            result[number] += 1
            Num = Num // N[number]

    print('#{} {}'.format(tc, ' '.join(map(str, result))))
