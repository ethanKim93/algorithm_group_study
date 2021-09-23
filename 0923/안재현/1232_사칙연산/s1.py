# 진행중

import sys
sys.stdin = open('input.txt')


for tc in range(10):
    N = int(input())
    NS = [list(input().split()) for _ in range(N)]
    result = 0
    for i in range(len(NS)):
        if type(n) == int:
            pass
        elif n == '+':
            result = calc(n) + calc(n)
        elif n == '-':
            result = calc(n) - calc(n)
        elif n == '/':
            result = calc(n) / calc(n)
        elif n == '*':
            result = calc(n) * calc(n)