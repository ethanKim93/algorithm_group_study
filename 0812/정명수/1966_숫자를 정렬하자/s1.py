import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(len(numbers)):
        min_idx = i
        for j in range(i,len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i],numbers[min_idx] = numbers[min_idx], numbers[i]

    print('#{}'.format(test_case), end=' ')
    print(*numbers)


