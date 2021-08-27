import sys
sys.stdin = open('input.txt')

def encrypt():
    while True:
        for i in range(1, 6):
            tmp = pw.pop(0)-i
            pw.append(tmp)
            if tmp <= 0:
                pw[-1] = 0
                return pw

for tc in range(1, 11):
    a = input()
    pw = list(map(int, input().split()))
    print('#{}'.format(tc), end=' ')
    print(*encrypt())