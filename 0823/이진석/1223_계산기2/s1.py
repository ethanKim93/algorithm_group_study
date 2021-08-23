import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    expression = input()    # 입력 수식
    postfix = []    # 후위표기식을 담을 배열
    operator = []   # 연산자 스택을 담을 배열
    top = -1
    for oper in expression:
        if oper == '+':         # +는 주어진 연산자 중 가장 우선순위가 낮으므로 연산자 스택에서 모두 pop
            while top > -1:
                postfix.append(operator.pop())
                top -= 1
            operator.append(oper)   # pop 이후에 스택에 push
            top += 1
        elif oper == '*':   # *는 +보다 우선순위가 높기 때문에 top에 *이 있을 경우에만 pop 한 후 스택에 push
            while top > -1 and operator[top] == '*':
                postfix.append(operator.pop())
                top -= 1
            operator.append(oper)
            top += 1
        else:       # 피연산자 모두 후위 표기식에 push
            postfix.append(int(oper))

    while operator: # 남은 연산자 모두 pop 후 후위 표기식에 push
        postfix.append(operator.pop())

    result = []     # 계산 결과 스택
    for oper in postfix:        # 후위 표기식 순회를 돌면서
        if oper == '+':         # 연산자는 필수적으로 피연산자 2개 이상 이후에 등장하므로
            a = result.pop()    # 연산결과 스택에서 2개를 pop해서 더하고 다시 push
            b = result.pop()
            c = a+b
            result.append(c)
        elif oper == '*':       # 마찬가지로 곱하기도 피연산자 2개를 pop 해서 곱한 후 다시 push
            a = result.pop()
            b = result.pop()
            c = a*b
            result.append(c)
        else:                   # 피연산자는 모두 push
            result.append(oper)

    print('#{} {}'.format(tc, result[0]))   # 연산결과 출력