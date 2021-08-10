import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    N = int(input())
    numbers=list(map(int, input().split()))
    max_num=numbers[0]
    min_num=numbers[0]
    for num in numbers:
        if num>max_num:
            max_num = num
        if num<min_num:
            min_num = num
    print('#{0} {1}'.format(i+1, max_num-min_num))


