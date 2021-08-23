# 후위 표기식 사용중 실패

import sys

sys.stdin = open("input.txt")

for i in range(0, 10):
    tc_len = int(input())
    tc = input()
    stack = []
    res = ''
    res2 = ''
    for x in tc:
        if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '0':
            res += x
        else:
            if x == '*' or x == '/' or x == '+' or x == '-':
                while stack:
                    res2 += stack.pop()
            stack.append(x)
    while stack:
        res2 += stack.pop()
    j = 0
    mul = 1
    result = 0
    while j <= len(res2):
        if res2[len(res2) - j - 1] == '+' and mul != 1:
            print(res[j])
            mul *= int(res[j])
            result += mul
            mul = 1
            j += 1
            print(result)
        elif res2[len(res2) - j - 1] == '+':
            print(res[j])
            result += int(res[j])
            j += 1
            print(result)
        elif res2[len(res2) - j - 1] == '*':
            print(res[j])
            mul *= int(res[j])
            j += 1
    print('#{} {}'.format(i + 1, result))