import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_number = numbers[0] #0번째 요소 최대값 설정
    min_number = numbers[0]
    for i in range(1, N):
        if max_number < numbers[i]: #최대값 비교
            max_number = numbers[i]

    for i in range(1, N):
        if min_number > numbers[i]: #최소값 비교
            min_number = numbers[i]
    print('#{} {}'.format(tc, max_number-min_number))