import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    a = input()

    N = input()
    num_list = [0]*10

    for n in N:
        num_list[int(n)] += 1

    big = 0

    for num in num_list:
        if num > big:
            big = num

    for i in range(10)[::-1]:
        if num_list[i] == big:
            break
    print('#{} {} {}'.format(tc, i, num_list[i]))
