import sys
sys.stdin = open('input.txt')

def change_to_dec(num, notation):
    tmp = 0

    for n,val in enumerate(list(map(int, num))[::-1]):
        tmp += val*(notation**n)
    return tmp

def check(num, notation):
    change_num = change_to_dec(num, notation)

    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(notation):
            if val == j : continue
            tmp = change_num - val * (notation**n) + j*(notation**n)

            if tmp not in binary:
                binary.append(tmp)
            else:
                return tmp

T = int(input())

for tc in range(1, T+1):
    bi = input()
    tr = input()

    binary = []
    check(bi, 2)

    print('#{} {}'.format(tc, check(tr, 3)))