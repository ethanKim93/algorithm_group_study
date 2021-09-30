import sys
sys.stdin = open('input.txt')

pwd_pattern = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    pwd_code = ''
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                pwd_code = arr[i][j-55:j+1]
                break

    pwd = []
    idx = 0
    for _ in range(8):
        pwd.append(pwd_pattern[pwd_code[idx:idx+7]])
        idx += 7

    verif = (pwd[0] + pwd[2] + pwd[4] + pwd[6]) * 3 + (pwd[1] + pwd[3] + pwd[5]) + pwd[7]

    if verif % 10:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, sum(pwd)))
