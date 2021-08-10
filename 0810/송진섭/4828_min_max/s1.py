import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_number = numbers[0]
    for i in range(1, len(numbers)):
        if max_number < numbers[i]:
            max_number = numbers[i]
    print('#{} {}'.format(tc, max_number))
