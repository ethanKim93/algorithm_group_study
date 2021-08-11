import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))


    for i in range(N-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    max_number = numbers[-1]
    min_number = numbers[0]
    print('#{} {}'.format(tc, max_number-min_number))