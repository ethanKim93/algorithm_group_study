import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 양수의 개수 N
    numbers = list(map(int, input().split()))

    max_num = numbers[0]  # numbers의 0번째 숫자를 임시로 max_num이라고 설정
    min_num = numbers[0]  # for문안에 들어가면 XX

    for number in numbers:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number

    total = max_num - min_num

    print('#{} {}'.format(test_case, total))




