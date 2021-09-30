import sys
sys.stdin = open('input.txt')

password = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4, "0110001": 5, "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    code = []
    flag = 0
    for _ in range(N):
        long_code_x = input()
        if flag:
            continue
        if '1' in long_code_x:
            long_code = long_code_x
            flag = 1
            continue

    for i in range(len(long_code)-1,0,-1):
        if long_code[i] == '1':
            break
    long_code = long_code[i-55:i+1]
    for k in range(0,56,7):
        password[long_code[k:k + 7]]
        code.append(password[long_code[k:k + 7]])
    check = (code[0]+code[2]+code[4]+code[6])*3+code[1]+code[3]+code[5]+code[7]

    if check % 10:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, sum(code)))



