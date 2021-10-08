import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    num2 = input()
    num3 = input()
    numbers = []
    int_num2 = int(num2,2)
    for i in range(len(num2)):
        if int_num2 & (1<<i):
            numbers.append(int(num2,2) - 2**i)
        else:
            numbers.append(int(num2,2) + 2**i)
    length = len(num3)
    int_num3 = int(num3,3)
    flag = 0
    for i in range(length):
        exclusive = num3[length-1-i]
        possible = ['0','1','2']
        check = int_num3 - int(exclusive)*(3**i)
        for j in possible:
            if j != exclusive:
                if check + int(j)*(3**i) in numbers:
                    answer = check + int(j)*(3**i)
                    flag = 1
                    break
        if flag:
            break
    print('#{} {}'.format(tc,answer))
