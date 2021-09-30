import sys
sys.stdin = open('input.txt')

pattern = {
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

for tc in range(1,T+1):
    N,M = map(int,input().split())
    for i in range(N):
        secret = input()
        if secret == '0'*M:continue
        else:
            code_key = ''
            for k in range(len(secret)-1,-1,-1):
                if secret[k] == '1':
                    code_key = secret[k-55:k+1]
                    break
    code = []
    while len(code) < 8:
        code.append(pattern[code_key[:7]])
        code_key = code_key[7:]
    ans = 0
    total_a = 0
    total_b = 0
    for m in range(7):
        if m%2:
            total_b += code[m]
        else:
            total_a += code[m]
    total = (total_a)*3 +total_b +code[7]
    if not total%10:
        ans = sum(code)
    print('#{} {}'.format(tc,ans))