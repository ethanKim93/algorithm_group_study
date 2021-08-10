import sys
sys.stdin = open("sample_input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    maxnum = numbers[0]
    minnum = numbers[0]
    for number in numbers:
        if number > maxnum:
            maxnum = number
        elif number < minnum:
            minnum = number

    print('#{} {}'.format(tc, maxnum-minnum))

