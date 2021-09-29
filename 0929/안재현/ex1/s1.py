# 0b : 2진수, 0o : 8진수, 0x : 16진수
# 이게 아닌가..

import sys
sys.stdin = open('input.txt')

cnt = 0
result = ''
a = input()
for i in range(len(a)):
    if cnt == 0:
        cnt += 1
    if cnt < 8:
        result += a[i]
        cnt += 1
    if cnt == 8:
        print(int("0b" + result, 2), end=' ')
        result = ''
        cnt = 0


