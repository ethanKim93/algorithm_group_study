

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    arr = []
    result=1      # 괄호 판단 변수
    for i in s:
        if i =='(' or i == '{': # 괄호가 있으면 lst에 담음
            arr.append(s)
        elif i == ')' or i == '}': # ) } 를 확인 했는데 전에 ( { 가 없으면 0 출력
            if len(arr)== 0:       # 리스트에 아무것도 들어 있지 않다면 0 출력
                result=0
                break
            else:
                b = arr.pop()         # 올바른 괄호를 판단하기 위한 변수
            if i == ')' and b =='{':  # )  일때 { 가 꺼내진다면 0 출력
                result=0
                break
            if i == '}' and b =='(':  # } 일때 ( 가 꺼내진다면 0 출력
                result=0
                break
    if len(arr):     # 남은 괄호가 있으면 0출력
        result=0

    print('#{} {}'.format(tc, result))







