import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    number = list(map(int, input().split()))

    for i in range(len(number) - 1):
        for j in range(i, len(number)):
            if number[i] > number[j]:
                number[i], number[j] = number[j], number[i]

    print("#{}".format(test_case), end=" ")
    print(*number)