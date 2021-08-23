# append, pop으로 활용!

import sys
sys.stdin = open("input.txt")

for _ in range(2):
    pair = str(input())

    stack = []
    for i in range(len(pair)):
        if pair[i] == '(':
            stack.append('*')
        else:
            if len(stack) == 0:
                print('괄호의 짝이 맞지 않습니다.')
            else:
                stack.pop(-1)

    if len(stack) == 0:
        print('괄호의 짝이 맞습니다.')
    else:
        print('괄호의 짝이 맞지 않습니다.')