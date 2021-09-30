# -*- coding: utf-8 -*-
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = float(input())    # 0 < N < 1의 입력값을 받음

    result = ''
    cnt = 1

    while True:
        # 12번을 초과하면 overflow 출력하고, while 문을 종료한다.
        if cnt > 12:
            result = 'overflow'
            break

        # 매 차례마다 N에 2를 곱한다.
        N *= 2

        # 2를 곱한 N이 1이 되면 더이상 확인하지 않아도 되므로
        #
        if N == 1:
            result += '1'
            break

        # 2를 곱한 N이 1보다 크면 N에 1을 빼주고,
        # 이진수로 표현한 결과값에 1를 붙여준다.
        elif N > 1:
            N -= 1
            result += '1'

        # 2를 곱한 N이 1보다 작으면 N은 그대로 두고,
        # 이진수로 표현한 결과값에 0를 붙여준다.
        else:
            result += '0'

        # cnt를 증가시켜준다.
        cnt += 1

    print('#{} {}'.format(tc, result))