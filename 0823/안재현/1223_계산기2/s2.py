# 일반 표기식 방식 성공

import sys

sys.stdin = open("input.txt")

for i in range(0, 10):
    tc_len = int(input())
    tc = input()
    temp = 0
    result = 0
    switch = 0
    empty_lst = []
    for j in tc:
        if j == '+':
            result += temp
            temp = 0
            switch = 0
        elif j == '*':
            if temp == 0:
                temp += 1
            switch = 1
        elif j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9' or j == '0':
            if switch == 0:
                temp += int(j)
            elif switch == 1:
                temp *= int(j)
    result += temp
    print('#{} {}'.format(i + 1, result))