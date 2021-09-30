import sys
sys.stdin = open('input.txt')
#1240.단순 2진 암호코드
password = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}
def decode(c):
    for i in range(0,56,7):
        tot.append(password[c[i:i+7]])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    for i in arr:
        if '1' in i:
            tot = []
            decode(i.rstrip('0')[-56:])
            break
    res = (tot[0] + tot[2] + tot[4] + tot[6])*3 + (tot[1] + tot[3] + tot[5])
    if (res+tot[-1]) % 10 == 0:
        print('#{} {}'.format(tc, sum(tot)))
    else:
        print('#{} 0'.format(tc))