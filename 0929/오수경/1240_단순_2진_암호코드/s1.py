import sys
sys.stdin = open('input.txt')

def find_code(i, j):
    global translate
    if len(translate) == 8:
        return translate
    else:
        for n in number:
            if code[i][j-6:j+1] == n:
                translate = str(number.index(n)) + translate
                find_code(i, j-7)
                return translate

def isitcode(amho):
    odd = 0
    even = 0
    verify_num = int(amho[-1])
    for i in range(7):
        if i%2 == 0:
            odd += int(amho[i])
        else:
            even += int(amho[i])
    if (odd*3 + even + verify_num)%10 == 0:
        return odd+even+verify_num
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]

    number = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']


    for i in range(N):
        translate = ''
        if '1' in code[i]:
            for j in range(M):
                if code[i][M-1-j] == '1':
                    print('#{} {}'.format(tc, isitcode(find_code(i, M-1-j))))
                    break
            break
