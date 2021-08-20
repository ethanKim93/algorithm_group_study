# -*- coding: utf-8 -*-

import sys

sys.stdin = open('input.txt')
T = 10

for tc in range(1, T + 1):
    numberlist = []
    N, numbers = input().split()

    for n in numbers:
        numberlist.append(n)
    stack = []
    play = 0

    while True:
        if play==len(numberlist)*len(numberlist):
            break

        for i in range(1, len(numberlist)):
            if i<len(numberlist) and numberlist[i] == numberlist[i - 1]:
                numberlist.pop(i)
                numberlist.pop(i-1)
        play+=1

    result=''.join(numberlist)

    print('#{} {}'.format(tc, result))
