import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = input()
    eq = input()                                    # 중위표기식 입력
    stack, post = [], []                            # stack: 연산자 스택, post: 후위표기식 스택
    for i in eq:                                    # 중위표기식에서 순회
        if i.isdecimal():                           # 피연산자(숫자)가 입력된 경우
            post.append(int(i))                     # 후위표기식 스택에 추가
        else:                                       # 연산자가 입력된 경우
            if i == '+':                            # '+' 연산자라면
                while stack:                        # 연산자 스택이 빌때까지
                    post.append(stack.pop())        # 연산자를 꺼내서 후위표기식에 추가
                stack.append(i)                     # 연산자 스택이 비면 비로소 현재 '+' 연산자를 연산자 스택에 추가
            else:                                   # '*' 연산자라면
                stack.append(i)                     # 바로 연산자 스택에 추가
    while stack:                                    # 중위표기식을 다 순회한 후에 연산자 스택에 연산자가 남아있으면
        post.append(stack.pop())                    # 남아있는 연산자를 하나씩 꺼내서 후위표기식에 추가

    for i in post:                                  # 후위표기식에서 순회
        if i == '+':                                # '+' 연산자라면
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)               # 스택에 있는 피연산자 두개를 꺼내서 더하고 그 결과를 스택에 추가
        elif i == '*':                              # '*' 연산자라면
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)               # 스택에 있는 피연산자 두개를 꺼내서 곱하고 그 결과를 스택에 추가
        else:
            stack.append(i)                         # 피연산자(숫자)라면 스택에 추가

    result = stack[0]
    print('#{} {}'.format(tc, result))              # 연산 후 마지막으로 남아있는 결과값을 출력