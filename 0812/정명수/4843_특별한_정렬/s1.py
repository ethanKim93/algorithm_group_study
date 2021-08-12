import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(0, len(numbers), 2):
        max_num = numbers[i]
        min_num = numbers[i]
        for j in range(i,len(numbers)):
            if numbers[j] > max_num:
                max_num = numbers[j]
                numbers[i], numbers[j] = numbers[j], numbers[i]

            if numbers[j] < min_num:
                min_num = numbers[j]
                numbers[i+1], numbers[j] = numbers[j], numbers[i+1]
    print('#{}'.format(test_case),end=' ')
    print(*numbers[0:10])

