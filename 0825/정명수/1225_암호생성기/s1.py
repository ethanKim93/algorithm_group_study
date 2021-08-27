import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    T = int(input())
    number = list(map(int,input().split()))
    i = 1
    while 1:
        new_number = number.pop(0)-i
        if new_number <= 0:
            number.append(0)
            break
        else:
            number.append(new_number)
        i += 1
        if i == 6:
            i = 1
    print('#{} '.format(tc),end='')
    print(*number)


